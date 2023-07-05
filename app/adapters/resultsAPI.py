from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/results/", tags= ["results"])
async def get_results():
    result_first = {"state_compute" : "Completed", "round_number" : 1, "registered" : 8765, "abstaining":65, "rate_abstaining":8.6}
    result_second = {"state_compute" : "Completed", "round_number" : 2, "registered" : 666, "abstaining":25, "rate_abstaining":12.6}
    results = [result_first, result_second]
    return results