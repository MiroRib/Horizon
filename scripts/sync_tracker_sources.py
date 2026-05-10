#!/usr/bin/env python3
"""
sync_tracker_sources.py
从 positions.json 动态注入 Tracker group 的 RSS sources 到 Horizon config.json。

用法：
  python sync_tracker_sources.py <positions.json> <config.json>

功能：
  1. 读取 positions.json 中的核心持仓标的（positions 字段）
  2. 为每个有仓位的标的生成 SEC EDGAR RSS feed
  3. 更新 config.json 的 rss sources 中 category="tracker" 的条目
  4. 不影响其他 sources 配置

注意：
  - 只处理 positions（核心跟踪），不处理 non_watchlist_positions
  - SEC EDGAR 的 CIK 号通过预定义映射表获取
  - 如果 positions.json 不可用，保留现有 tracker 配置不变
"""

import json
import sys
from pathlib import Path

# 已知标的的 SEC EDGAR CIK 映射
# 新增标的时在这里添加，或由 Peter 自动维护
TICKER_TO_CIK = {
    "APP": "0001498148",   # AppLovin Corporation
    "BE": "0001664703",    # Bloom Energy Corporation
    "GEV": "0001974446",   # GE Vernova Inc
    "PDD": "0001737806",   # PDD Holdings Inc (ADR)
    "AMZN": "0001018724",  # Amazon.com Inc
    "NVDA": "0001045810",  # NVIDIA Corp
    "INTC": "0000050863",  # Intel Corp
    "RBLX": "0001315098",  # Roblox Corp
    "QCOM": "0000804328",  # Qualcomm Inc
    "SEI": "0000350894",   # SEI Investments (placeholder - verify CIK)
}

# 已知标的的公司全名映射（用于 source name）
TICKER_TO_NAME = {
    "APP": "AppLovin Corporation",
    "BE": "Bloom Energy Corporation",
    "GEV": "GE Vernova Inc",
    "PDD": "PDD Holdings Inc",
    "AMZN": "Amazon.com Inc",
    "NVDA": "NVIDIA Corp",
    "INTC": "Intel Corp",
    "RBLX": "Roblox Corp",
    "QCOM": "Qualcomm Inc",
    "SEI": "SEI Investments",
}


def build_sec_rss_url(cik: str) -> str:
    """构建 SEC EDGAR Atom feed URL"""
    return (
        f"https://www.sec.gov/cgi-bin/browse-edgar?"
        f"action=getcompany&CIK={cik}&type=&dateb=&owner=include"
        f"&count=10&search_text=&output=atom"
    )


def get_active_tickers(positions_data: dict) -> list[str]:
    """从 positions.json 提取有实际仓位的核心标的 ticker"""
    active = []
    positions = positions_data.get("positions", {})
    
    for ticker, data in positions.items():
        # 检查是否有实际仓位（非零 shares 或有 options）
        has_position = False
        
        # 检查各账户
        for account_key in ["SR", "GDM"]:
            account = data.get(account_key, {})
            
            # 检查 equity
            equity = account.get("equity", {})
            shares = equity.get("shares")
            if shares and shares > 0:
                has_position = True
                break
            
            # 检查 options
            options = account.get("options", [])
            if options:
                has_position = True
                break
        
        # 也检查 combined
        combined = data.get("combined", {})
        total_shares = combined.get("total_shares")
        if total_shares and total_shares > 0:
            has_position = True
        
        if has_position:
            active.append(ticker)
    
    return active


def generate_tracker_sources(tickers: list[str]) -> list[dict]:
    """为活跃标的生成 tracker RSS sources"""
    sources = []
    
    for ticker in tickers:
        cik = TICKER_TO_CIK.get(ticker)
        if not cik:
            print(f"  [WARN] No CIK mapping for {ticker}, skipping SEC EDGAR source")
            continue
        
        name = TICKER_TO_NAME.get(ticker, ticker)
        sources.append({
            "name": f"SEC EDGAR - {ticker} ({name})",
            "url": build_sec_rss_url(cik),
            "enabled": True,
            "category": "tracker"
        })
    
    return sources


def update_config(config_path: Path, tracker_sources: list[dict]) -> None:
    """更新 config.json 中的 tracker sources"""
    with open(config_path, "r") as f:
        config = json.load(f)
    
    # 获取现有 RSS sources
    rss_sources = config.get("sources", {}).get("rss", [])
    
    # 移除旧的 tracker category sources
    non_tracker = [s for s in rss_sources if s.get("category") != "tracker"]
    
    # 合并新的 tracker sources
    updated_rss = non_tracker + tracker_sources
    config["sources"]["rss"] = updated_rss
    
    # 写回
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"  [OK] Updated config with {len(tracker_sources)} tracker sources")


def main():
    if len(sys.argv) < 3:
        print("Usage: python sync_tracker_sources.py <positions.json> <config.json>")
        sys.exit(1)
    
    positions_path = Path(sys.argv[1])
    config_path = Path(sys.argv[2])
    
    if not positions_path.exists():
        print(f"  [WARN] positions.json not found at {positions_path}, keeping existing config")
        sys.exit(0)
    
    if not config_path.exists():
        print(f"  [ERROR] config.json not found at {config_path}")
        sys.exit(1)
    
    # 读取 positions
    with open(positions_path, "r") as f:
        positions_data = json.load(f)
    
    # 提取活跃标的
    active_tickers = get_active_tickers(positions_data)
    print(f"  Active tickers from positions.json: {active_tickers}")
    
    # 生成 tracker sources
    tracker_sources = generate_tracker_sources(active_tickers)
    
    # 更新 config
    update_config(config_path, tracker_sources)
    
    print(f"  Done. Tracker group now monitors: {[t for t in active_tickers if t in TICKER_TO_CIK]}")


if __name__ == "__main__":
    main()
