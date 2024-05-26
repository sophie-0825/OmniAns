import json
from asyncflows.actions.base import Action, BaseModel, Field
from typing import Any

class Inputs(BaseModel):
    json_string: str = Field(
        description="JSON-like string to be transformed into JSON",
    )

class Outputs(BaseModel):
    json_object: Any = Field(
        description="Resulting JSON object",
    )

class LoadJSON(Action[Inputs, Outputs]):
    name = "load_json"

    async def run(self, inputs: Inputs) -> Outputs:
        try:
            json_object = json.loads(inputs.json_string)
        except json.JSONDecodeError as e:
            self.log.error("Failed to parse json",
            data=inputs.json_string)
            raise ValueError(f"Invalid JSON string: {e}")
        return Outputs(json_object=json_object)

# Example usage:
# inputs = Inputs(json_string='{"key": "value"}')
# action = LoadJSON()
# result = await action.run(inputs)
# print(result.json_object)  # Outputs: {'key': 'value'}