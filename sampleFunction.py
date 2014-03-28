__author__ = 'yiminggu'
config = {'base_url':'http://www.mikehibbert.me.uk','pages':['home','about','contact']}

def base_url():
    return config['base_url']




def get_page_url(name):
    page_name = ''
    if name in config['pages']:
        page_name = name

    return "%s/%s" % (base_url(), page_name)





print config['base_url']
print config['pages'][1]