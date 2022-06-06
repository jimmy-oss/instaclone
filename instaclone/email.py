from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = ' 𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓽𝓱𝓮 ✴  🎀  𝒜𝒹𝓋𝑒𝓃𝑔𝒾𝓈𝓈  🎀  ✴  𝓝𝓮𝔀𝓼𝓛𝓮𝓽𝓽𝓮𝓻'
    sender = 'jimmyjammie48@gmail.com' 
    #passing in the context vairables
    text_content = render_to_string('/templates/email/email.txt',{"name": name})
    html_content = render_to_string('/templates/email/email.html',{"name": name})
    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
