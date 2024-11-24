from clearml import PipelineDecorator

from project.steps.etl import crawl_links


@PipelineDecorator
def digital_data_etl(links: list[str]) -> str:
    last_step = crawl_links(links=links)

    return last_step.invocation_id


digital_data_etl(["https://github.com/ros-infrastructure/www.ros.org/"])
