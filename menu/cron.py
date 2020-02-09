from menu.management.commands.crawl_menu import crawl_snu


def crawl_menu_cron():
    crawl_snu()
