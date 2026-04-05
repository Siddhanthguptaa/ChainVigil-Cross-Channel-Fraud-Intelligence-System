import asyncio
from backend.main import run_full_pipeline

async def test():
    res = await run_full_pipeline()
    print("AUC:", res.details["training"]["best_val_auc"])
    print("Flags:", res.details["risk"]["flagged"])
    print("Clusters:", res.details["risk"]["clusters"])

asyncio.run(test())
