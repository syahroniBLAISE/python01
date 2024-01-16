msg_template = """Hello {name},
<h1>Thank you</h1> for joining {website}. We are very
happy to have you with us.
""" # .format(name="Justin", website='cfe.sh')


def format_msg(my_name="roni", my_website="syahroni.tech"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg
