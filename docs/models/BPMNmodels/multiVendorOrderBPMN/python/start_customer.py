
import asyncio
from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ProcessCreationById,
)

async def main():
    async with CamundaAsyncClient(
        configuration={"CAMUNDA_LOAD_ENVFILE": "true"}
    ) as client:

        process_data = ProcessCreationById.from_dict({
            "processDefinitionId": "Process_18mlly9",
            "variables": {
                "customerOrder": {
                    "orderId": "ORD008",
                    "customerId": "C001",
                    "orderDate": "2026-11-18",
                    "requestedFulfilmentDate": "2026-11-20",
                    "fulfilmentMethod": "Collection",
                    "orderItems": [
                        {
                            "productId": "P001",
                            "requestedQuantity": 20
                        },
                        {
                            "productId": "P005",
                            "requestedQuantity": 2
                        }
                    ]
                }
            }
        })

        result = await client.create_process_instance(
            data=process_data
        )

        print("Customer process started successfully!")
        print("Instance key:", result.process_instance_key)

if __name__ == "__main__":
    asyncio.run(main())
