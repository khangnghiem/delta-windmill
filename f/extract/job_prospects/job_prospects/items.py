# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Identity
from w3lib.html import remove_tags


class DataIngestionItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobProspectLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(str.strip, remove_tags)

class JobProspectItem(Item):
    link = Field()
    title = Field()
    company_name = Field()
    company_address = Field()
    company_map_link = Field()
    company_size = Field()
    company_contact = Field()
    area = Field(output_processor=Identity())
    views = Field()
    expiry_date = Field()
    job_description = Field(output_processor=Identity())
    job_requirements = Field(output_processor=Identity())
    job_posted_date = Field()
    job_department = Field()
    job_field = Field()
    job_minimum_experience = Field()
    job_level = Field()
    job_skills = Field()
    document_language = Field()
    nationality = Field()
    work_address = Field()
    tags = Field(output_processor=Identity())


class CompanyOverviewLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(str.strip, remove_tags)


class CompanyOverviewItem(Item):
    link = Field()
    website = Field()
    phone_number = Field()
    department = Field()
    business_type = Field()
    headquarter = Field()
    scale = Field()
    revenue = Field()
    established_at = Field()
    description = Field()
    insurance_policies = Field()
    activities = Field()
    background_history = Field()
    mission = Field()
    parent = Field()
    parent_headquarter = Field()


class CompanyReviewLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(str.strip, remove_tags)


class CompanyReviewItem(Item):
    link = Field()
    review_rating = Field()
    review_title = Field()
    review_position = Field()
    review_date = Field()
    pros = Field()
    cons = Field()


class CompanyLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(str.strip, remove_tags)


class CompanyItem(Item):
    link = Field()
    name = Field()
    location = Field()
    department = Field()
    scale = Field()
