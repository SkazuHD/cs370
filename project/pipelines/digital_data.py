import sys

# sys.path.append("/workspaces/eng-ai-agents/project")
# sys.path.append("/workspaces/eng-ai-agents/project/steps")


print("PATH:", sys.path)

from steps.etl import crawl_links


# @PipelineDecorator(project="TEST", name="ETL")
def digital_data_etl(links: list[str]) -> str:
    pass
    last_step = crawl_links(links=links)

    return last_step.invocation_id


# digital_data_etl(["https://github.com/ros-infrastructure/www.ros.org/"])
