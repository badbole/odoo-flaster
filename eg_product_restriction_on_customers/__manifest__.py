{
    "name": "Product Restriction on Customer",

    'version': "16.0",

    'category': "Product",

    "summary": "This app will Restrict selected Products for particular Customer.",
    
    'author': "INKERP",

    'website': "https://www.INKERP.com",

    "depends": ['product'],
    
    "data": [
        "security/security.xml",
        "views/res_partner_view.xml",
    ],


    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
