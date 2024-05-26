import json
from asyncflows.actions.base import Action, BaseModel, Field
from typing import Any

class Inputs(BaseModel):
    string: str

class Outputs(BaseModel):
    string: str

class LoadJSON(Action[Inputs, Outputs]):
    name = "create_string"

    async def run(self, inputs: Inputs) -> Outputs:
        return Outputs(string=inputs.string)

