import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), './classes'))
from company_info import Info
from gmail import Gmail
from template_builder import Builder

info = Info ()
mail = Gmail()
template = Builder ()

# The URL of the IEX Cloud API from where to get the data

stockURL = 'https://cloud.iexapis.com/stable/stock/'

# The symbols of the stock you want updates from - Here, Microsoft, Visa, Nike, Novartis and Zoom

symbols = ['MSFT','V', 'NKE','NOVN','ZM']
summary = []
articles = []
companyName = []
exchange = []

try:

    # Get the latest articles

    for i in symbols:

        summary.append(info.get_summary(i,stockURL))
        articles.append(info.get_articles(i, stockURL))
        companyName.append(info.get_company_name(i, stockURL))
        exchange.append(info.get_exchange(i, stockURL))

    # Build jinja2 template

    email_body = template.build_template(symbols, summary, articles, companyName, exchange)

    # Send email

    mail.send_email(email_body)

    print ('Email sent!')

except Exception as e:

    # Print the thrown error

    print("Error in the app.py file: " + str(e))
