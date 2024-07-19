# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from random import randint
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class Candy(BaseModel):
    id: int
    size: int


class CandySet(BaseModel):
    id: int
    candies: List[Candy]


candy_sets = {}


@app.get("/candies/{candy_set_id}")
def get_candies(candy_set_id: int):
    global candy_sets
    candies = [Candy(id=i, size=randint(1, 10)) for i in range(6)]
    candy_set = CandySet(id=candy_set_id, candies=candies)
    candy_sets[candy_set_id] = candy_set
    return candy_set


@app.post("/lick/{candy_set_id}")
def lick_candies(candy_set_id: int):
    global candy_sets
    if candy_set_id not in candy_sets:
        raise HTTPException(status_code=404, detail="Candy set not found")
    candy_set = candy_sets[candy_set_id]
    for candy in candy_set.candies:
        candy.size -= randint(0, 3)
        if candy.size < 0:
            candy.size = 0
    return candy_set


@app.post("/bite/{candy_set_id}")
def bite_candy(candy_set_id: int):
    """
    Bite a candy from a candy set
    """
    # 1. Only candies of size < 5 can be bitten
    # 2. The size of the candy gets reduced
    # 3. The size of the candy is never negative
    # 4. You can't bite a candy that's 0 in size
    # 5. Each bite will reduce the size of the candy by 3 to 5
    bite = False
    global candy_sets
    if candy_set_id not in candy_sets:
        raise HTTPException(status_code=404, detail="Candy set not found")
    candy_set = candy_sets[candy_set_id]
    for candy in candy_set.candies:
        if candy.size < 5 and candy.size > 0:
            bite = True
            candy.size -= randint(3, 5)
            if candy.size < 0:
                candy.size = 0
    if not bite:
        raise HTTPException(status_code=400, detail="No candies can be bitten")
    return candy_set
