
import asyncio

from camunda_orchestration_sdk import CamundaAsyncClient
from workers import register_workers


async def main():
    async with CamundaAsyncClient(
        configuration={
            "CAMUNDA_LOAD_ENVFILE": "true"
        }
    ) as client:

        register_workers(client)

        print("BRFN workers started. Waiting for jobs...")

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())
