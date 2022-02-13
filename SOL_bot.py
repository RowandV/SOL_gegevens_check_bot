import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import pandas as pd
import numpy as np
data = pd.read_csv('Aanvullende_gegevens.csv', sep=';')

#Verander alle lege velden in LEEG zodat het duidelijk is voor de lezer en code.
data = data.replace(np.nan, 'LEEG', regex=True)

print("Dataframe columns:", data.columns)

# Verander de namen van de colomen zodat er geen spaties meer in zitten en geen tekens zoals '-'
data = data.rename(columns={"Lid initialen":"initialen"})
data = data.rename(columns={"Lid achternaam":"achternaam"})
data = data.rename(columns={"Lid tussenvoegsel":"tussenvoegsel"})

data = data.rename(columns={"Lid voornaam":"voornaam"})
data = data.rename(columns={"Lid aanvullende adresgegevens":"aanvullende_adresgegevens"})
data = data.rename(columns={"Lid adres":"adres"})

data = data.rename(columns={"Lid straat":"straat"})
data = data.rename(columns={"Lid huisnummer":"huisnummer"})
data = data.rename(columns={"Lid toevoegsel huisnr":"toevoegsel_huisnr"})
data = data.rename(columns={"Lid postcode":"postcode"})

data = data.rename(columns={"Lid plaats":"plaats"})
data = data.rename(columns={"Lid land":"land"})
data = data.rename(columns={"Lid geboortedatum":"geboortedatum"})
data = data.rename(columns={"Lid geboorteplaats":"geboorteplaats"})

data = data.rename(columns={"lid geboorteland":"geboorteland"})
data = data.rename(columns={"Lid geslacht":"geslacht"})
data = data.rename(columns={"Lid telefoon":"telefoon"})
data = data.rename(columns={"Lid mobiel":"mobiel"})

data = data.rename(columns={"Lid e-mailadres":"emailadres"})
data = data.rename(columns={"Lid naam ouder/verzorger 1":"naam_ouder1"})

data = data.rename(columns={"Lid telefoonnummer ouder/verzorger 1":"telefoonnummer_ouder1"})

data = data.rename(columns={"Lid e-mailadres ouder/verzorger 1":"emailadres_ouder1"})
data = data.rename(columns={"Lid naam ouder/verzorger 2":"naam_ouder2"})
data = data.rename(columns={"Lid telefoonnummer ouder/verzorger 2":"telefoonnummer_ouder2"})

data = data.rename(columns={"Lid e-mailadres ouder/verzorger 2":"emailadres_ouder2"})
data = data.rename(columns={"Lid ziektekostenverzekeraar":"ziektekostenverzekeraar"})
data = data.rename(columns={"Lid ziektekostenpolis nummer":"ziektekostenpolis_nummer"})

data = data.rename(columns={"Functie startdatum":"Functie_startdatum"})
data = data.rename(columns={"Overige informatie":"Overige_informatie"})

data = data.rename(columns={"Aanvullende lidgegevens gewijzigd op":"Aanvullende_lidgegevens_gewijzigd_op"})

data = data.rename(columns={"Lid mag op de foto voor: - Social Media":"Social_Media"})
data = data.rename(columns={"Lid mag op de foto voor: - Social Media":"Social_Media"})
data = data.rename(columns={"Lid mag op de foto voor: - Social Media":"Social_Media"})
data = data.rename(columns={"Lid mag op de foto voor: - Social Media":"Social_Media"})
data = data.rename(columns={"Lid mag op de foto voor: - Social Media":"Social_Media"})
data = data.rename(columns={"Lid mag op de foto voor: - Website":"Website"})
data = data.rename(columns={"Lid mag op de foto voor: - Whatsapp":"Whatsapp"})
data = data.rename(columns={"Lid mag op de foto voor: - Helemaal niet":"Helemaal_niet"})
data = data.rename(columns={"Lid mag op de foto voor: - Anders namelijk: -":"Anders_"})
data = data.rename(columns={"Lid mag op de foto voor: - Anders namelijk:":"Anders"})

data = data.rename(columns={"Naam huisarts":"Naam_huisarts"})

aantal_rijen = data.shape[0]

# Hier start de loep die voor elk lid aan de slag gaat
# ind is hier kort voor index om bij te houden bij welke rij we zijn van de data.
for ind in range(aantal_rijen):
    #Als het lid een tussenvoegsel heeft dan komt die in de naam, zo niet dan niet:
    if data.loc[ind].tussenvoegsel=="LEEG":
        naam = data.loc[ind].voornaam+" "+data.loc[ind].achternaam
    else:
        naam = data.loc[ind].voornaam+" "+data.loc[ind].tussenvoegsel+ " "+data.loc[ind].achternaam
    
    # Voor de mail inhoud is het goed om te weten dat """ gebruikt wordt wanneer de tekst over 
    # meerdere regels gaat en een enkele " gebruikt mag worden als er geen enters in zitten.
    # Sommige getallen, zoals telefoonnummers worden door panda's niet herkend als tekst. 
    # Het wordt naar tekst geconverteerd met str()
    
    mailInhoud = "Beste ouders/verzorgers van "+naam+""",

    Graag willen wij de gegevens van onze leden actueel houden, en wij vragen uw hulp om de gegevens van uw kind te controleren. Dit vragen wij van u zodat, in het algemeen en bijvoorbeeld in geval van nood, alle informatie bekend is bij ons. Hieronder staan alle gegevens die op dit moment bij ons bekend zijn, dit staat in het ledenadministratie systeem van scouting Nederland, Scouts Online (SOL). 
    In de bijlage kunt u een handleiding vinden over SOL, hierin staat hoe u een account aan kan maken en waar alle gegevens staan. 

    We ontvangen graag een mailtje terug, zodat we weten dat ons mailtje goed aan is gekomen.

    Basis gegevens
    Hieronder staan de basisgegevens van uw kind. Dit zijn naam, geboortedatum, telefoonnummer, email en adres.
    Voornaam:           """+data.loc[ind].voornaam+ """
    Tussenvoegsel:      """+data.loc[ind].tussenvoegsel+ """
    Achternaam:         """+data.loc[ind].achternaam+ """
    Initialen:          """+data.loc[ind].initialen+"""
    Geboortedatum:      """+data.loc[ind].geboortedatum+"""
    Geboorteplaats:     """+data.loc[ind].geboorteplaats+"""
    Geboorteland:       """+data.loc[ind].geboorteland+"""

    Telefoon (huisnummer): """+str(data.loc[ind].telefoon)+"""
    Mobiel (eigen nummer): """+str(data.loc[ind].mobiel)+"""
    E-mailadres:           """+data.loc[ind].emailadres+"""

    Adres:                 """+data.loc[ind].adres+"""
    Postcode:              """+data.loc[ind].postcode+"""
    Plaats:                """+data.loc[ind].plaats+"""

    Hieronder staan de gegevens van de ouders/verzorgers. Achter de kopjes staan de cijfers 1 of 2, dit wil zeggen dat wij ouder/verzorger 1 als eerste bellen, mocht dat nodig zijn. Mocht ouder/verzorger 1 niet beschikbaar zijn, dan bellen wij nummer 2.

    Naam ouder/verzorger 1:           """+data.loc[ind].naam_ouder1+"""
    Telefoonnummer ouder/verzorger 1: """+str(data.loc[ind].telefoonnummer_ouder1)+"""
    E-mailadres ouder/verzorger 1:    """+data.loc[ind].emailadres_ouder1+"""

    Naam ouder/verzorger 2:           """+data.loc[ind].naam_ouder2+"""
    Telefoonnummer ouder/verzorger 2: """+str(data.loc[ind].telefoonnummer_ouder2)+"""
    E-mailadres ouder/verzorger 2:    """+data.loc[ind].emailadres_ouder2+"""

    Ziektekostenverzekeraar:          """+data.loc[ind].ziektekostenverzekeraar+"""
    Ziektekostenpolis nummer:         """+data.loc[ind].ziektekostenpolis_nummer+"""  

    Hieronder kunt u de overige belangrijke informatie toevoegen zoals allergieen. Het kan zijn dat hier al iets staat over wel of niet op de foto mogen of de huisarts, dit kan verwijderd worden, hiervoor is later een apart kopje.

    Overige informatie:     """+data.loc[ind].Overige_informatie+"""

    Aanvullende gegevens 
    Hieronder staat of de foto van uw zoon/dochter mag worden gedeeld via social media en whatsapp en of de foto op de website gebruikt mag worden. Bij de meeste leden is dit nog niet ingevuld. Als het wel is ingevuld betekent een 1.0 ja en 0.0 betekend nee.

    Lid mag op de foto voor: - Social Media:    """+str(data.loc[ind].Social_Media)+"""
    Lid mag op de foto voor: - Website:         """+str(data.loc[ind].Website)+"""
    Lid mag op de foto voor: - Whatsapp:        """+str(data.loc[ind].Whatsapp)+"""
    Lid mag op de foto voor: - Helemaal niet:   """+str(data.loc[ind].Helemaal_niet)+"""
    Lid mag op de foto voor: - Anders namelijk: """+str(data.loc[ind].Anders_)+"""
    Lid mag op de foto voor: - Anders namelijk: """+str(data.loc[ind].Anders)+"""

    Als laatste de naam van de huisarts.

    Naam huisarts:   """+data.loc[ind].Naam_huisarts+"""


    Mochten er onduidelijkheden zijn, of komt u er niet uit. Stuur dan een mail naar scouts@scoutingzuidlaren.nl 

    Met vriendelijke groet, 
    De scoutsleiding
    """
    #print(mailInhoud)

    #Mail verzend code gebaseerd op: https://pythonprogramming.altervista.org/send-a-pdf-with-an-email-with-python/
    
    body = mailInhoud
    # put your email here
    sender = 'uw_email_adres@gmail.com'
    # get the password in the gmail (manage your google account, click on the avatar on the right)
    # then go to security (right) and app password (center)
    # insert the password and then choose mail and this computer and then generate
    # copy the password generated here
    password = 'Uw wachtwoord'
    # put the email of the receiver here
    receiver = data.loc[ind].emailadres_ouder1

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Gegevens controleren scouting'

    message.attach(MIMEText(body, 'plain'))

    pdfname = 'Handleiding voor SOL V3.pdf'

    # open the file in bynary
    binary_pdf = open(pdfname, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    # payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())

    # enconding the binary into base64
    encoders.encode_base64(payload)

    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)

    #use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)

    #enable security
    session.starttls()

    #login with mail_id and password
    session.login(sender, password)

    text = message.as_string()
    session.sendmail(sender, receiver, text)
    print(mailInhoud)
    session.quit()
    print('Mail Sent')