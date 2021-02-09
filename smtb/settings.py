BOT_NAME = 'smtb'
SPIDER_MODULES = ['smtb.spiders']
NEWSPIDER_MODULE = 'smtb.spiders'
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
   'smtb.pipelines.DatabasePipeline': 300,
}
FEED_EXPORT_ENCODING = 'utf-8'
