from flask import Flask ,render_template,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
#import openai
#from transformers import pipelines


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'#here we created a database using sqllit
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

app.app_context().push()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

class Todo_1(db.Model):
    sno_1 = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(200), nullable=False)
    pid = db.Column(db.String(100), nullable=False)
    add = db.Column(db.String(500), nullable=False)
    cnr = db.Column(db.String(100), nullable=False)
    advo = db.Column(db.String(200), nullable=False)
    advo_id = db.Column(db.String(100), nullable=False)
    o_pname = db.Column(db.String(200), nullable=False)
    o_pid = db.Column(db.String(100), nullable=False)
    o_add = db.Column(db.String(500), nullable=False)
    o_advo = db.Column(db.String(200), nullable=False)
    o_advo_id = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno_1}-{self.pname}"
class Law_Table(db.Model):
    sno_2 = db.Column(db.Integer, primary_key=True)
    advocate_name = db.Column(db.String(200), nullable=False)
    advocate_id = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(500), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    advocate_type = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    # total_cases = db.Column(db.Integer, nullable=False)
    won_cases = db.Column(db.Integer, nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.sno_2}-{self.advocate_name}"
       
@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
      title=request.form['title']
      desc=request.form['desc']
      todo=Todo(title=title,desc=desc)
      db.session.add(todo)
      db.session.commit()

    
    allTodo=Todo.query.all()
    print(allTodo)
    return render_template('index.html',allTodo=allTodo)
  #  return 'Hello, World!'

@app.route('/case', methods=['GET', 'POST'])
def case():
    if request.method == 'POST':
        pname = request.form['pname']
        pid = request.form['pid']
        add = request.form['add']
        cnr = request.form['cnr']
        advo = request.form['advo']
        advo_id = request.form['advo_id']
        o_pname = request.form['o_pname']
        o_pid = request.form['o_pid']
        o_add = request.form['o_add']
        o_advo = request.form['o_advo']
        o_advo_id = request.form['o_advo_id']

        todo_1 = Todo_1(
            pname=pname, pid=pid, add=add, cnr=cnr,
            advo=advo, advo_id=advo_id, o_pname=o_pname,
            o_pid=o_pid, o_add=o_add, o_advo=o_advo,
            o_advo_id=o_advo_id
        )
        db.session.add(todo_1)
        db.session.commit()

    allTodo_1 = Todo_1.query.all()
    return render_template('case.html', allTodo_1=allTodo_1)
@app.route('/allcases', methods=['GET', 'POST'])
def case1():
    if request.method == 'POST':
        pname = request.form['pname']
        pid = request.form['pid']
        add = request.form['add']
        cnr = request.form['cnr']
        advo = request.form['advo']
        advo_id = request.form['advo_id']
        o_pname = request.form['o_pname']
        o_pid = request.form['o_pid']
        o_add = request.form['o_add']
        o_advo = request.form['o_advo']
        o_advo_id = request.form['o_advo_id']

        todo_1 = Todo_1(
            pname=pname, pid=pid, add=add, cnr=cnr,
            advo=advo, advo_id=advo_id, o_pname=o_pname,
            o_pid=o_pid, o_add=o_add, o_advo=o_advo,
            o_advo_id=o_advo_id
        )
        db.session.add(todo_1)
        db.session.commit()

    allTodo_1 = Todo_1.query.all()
    return render_template('allcases.html', allTodo_1=allTodo_1)

@app.route('/court')
def Court():
    return render_template('court.html')
#Judge module
@app.route('/case',methods=['POST'])
def file_case():
    if request.method =='POST':
        return render_template('case.html')

@app.route('/case')
def update_case():
    return render_template('allcases.html')

@app.route('/Lawyer_registration')
def opposition_update():
    return render_template('Lawyer_registration.html')

@app.route('/allcases')
def view_case():
    return render_template('allcases.html')
#judge module end
#Adding lawer 
@app.route('/lawyers',methods=['GET', 'POST'])
def lawyer_registeration():
    if request.method =='POST':
        advocate_name=request.form['advocate_name']
        advocate_id=request.form['advocate_id']
        email=request.form['email']
        phone=request.form['phone']
        advocate_type=request.form['advocate_type']
        location=request.form['location']
        # total_cases=request.form['total_cases']
        won_cases=request.form['won_cases']
        
        law_table = Law_Table(
            advocate_name=advocate_name,advocate_id=advocate_id,email=email,phone=phone,advocate_type=advocate_type,
            location=location,won_cases=won_cases
        )
        db.session.add(law_table)
        db.session.commit()
    law_table_2 = Law_Table.query.all()
    return render_template('lawyers.html',law_table_2=law_table_2)
    

@app.route('/Lawyer_registration',methods=['GET', 'POST'])
def lawyer_Listing():
    if request.method =='POST':
        advocate_name=request.form['advocate_name']
        advocate_id=request.form['advocate_id']
        email=request.form['email']
        phone=request.form['phone']
        advocate_type=request.form['advocate_type']
        location=request.form['location']
        # total_cases=request.form['total_cases']
        won_cases=request.form['won_cases']
        
        law_table = Law_Table(
            advocate_name=advocate_name,advocate_id=advocate_id,email=email,phone=phone,advocate_type=advocate_type,
            location=location,won_cases=won_cases
        )
        db.session.add(law_table)
        db.session.commit()
    law_table_2 = Law_Table.query.all()
    return render_template('Lawyer_registration.html',law_table_2=law_table_2)

#registration of lawer

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo.title = title
        todo.desc = desc
        db.session.commit()
        return redirect("/")
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/delete_case/<int:sno_1>')
def delete_case(sno_1):
    todo=Todo_1.query.filter_by(sno_1=sno_1).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/case")

@app.route('/delete_law/<int:sno_2>')
def delete_law(sno_2):
    todo=Law_Table.query.filter_by(sno_2=sno_2).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/lawyers")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    bot_response = generate_response(user_message)
    return jsonify({'response': bot_response})
# Load the NLP model for question answering
#nlp = pipelines("question-answering")
def generate_response(message):
    message = message.lower().strip()
    if message in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today?"
    elif message in ["how are you?", "how are you"]:
        return "I'm a chatbot, so I don't have feelings, but thanks for asking! How can I help you?"
    elif message in ["what is your name?", "who are you?"]:
        return "I am your friendly chatbot. How can I assist you?"
    elif message in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    elif message in ["Article_21","Article21"]:
        return "Article 21 guarantees the protection of life and personal liberty. It states that no person shall be deprived of his life or personal liberty except according to the procedure established by law"
    elif "weather" in message:
        return "I can't check the weather right now, but you can check a weather app for current conditions."
    elif "joke" in message:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif message in ["What is Section 302 of the Indian Penal Code?"]:
        return "Section 302 of the IPC deals with punishment for murder. It prescribes the death penalty or life imprisonment and a fine for those convicted of murder."
    elif message == "Can you explain Section 420 of the IPC?":
        return "Section 420 of the IPC addresses cheating and dishonestly inducing delivery of property. It prescribes punishment for those involved in fraudulent activities."
    elif message == "What is the Juvenile Justice Act?":
        return "The Juvenile Justice Act deals with the care, protection, and rehabilitation of children in conflict with the law and those in need of care and protection."
    elif message == "What does Section 498A of the IPC cover?":
        return "Section 498A deals with the harassment of a married woman by her husband or his relatives, which includes cruelty and demands for dowry."
    elif message == "What is the purpose of the RTI Act?":
        return "The Right to Information (RTI) Act empowers citizens to request information from public authorities, promoting transparency and accountability in governance."
    elif message == "What does the Indian Contract Act regulate?":
        return "The Indian Contract Act governs the formation, performance, and enforcement of contracts in India."
    elif message == "What is Section 377 of the IPC?":
        return "Section 377 of the IPC was historically used to criminalize unnatural sexual offenses. It was partially decriminalized by the Supreme Court in 2018."
    elif message == "What is the Protection of Human Rights Act?":
        return "The Protection of Human Rights Act established the National Human Rights Commission (NHRC) to investigate human rights violations and ensure protection."
    elif message == "What does Section 12 of the CrPC relate to?":
        return "Section 12 of the Criminal Procedure Code (CrPC) allows the police to arrest without a warrant in certain cases where it is deemed necessary."
    elif message == "What is the Companies Act?":
        return "The Companies Act regulates the formation, operation, and dissolution of companies in India."
    elif message == "What does the Consumer Protection Act aim to do?":
        return "The Consumer Protection Act aims to safeguard consumers' rights and address grievances against unfair trade practices."
    elif message == "What is Section 125 of the CrPC?":
        return "Section 125 of the CrPC provides for maintenance to be given by a person to his wife, children, or parents if they are unable to maintain themselves."
    elif message == "Can you explain the Insolvency and Bankruptcy Code?":
        return "The Insolvency and Bankruptcy Code provides a legal framework for insolvency resolution and bankruptcy proceedings for individuals and companies."
    elif message == "What is the Intellectual Property Rights Act?":
        return "This Act provides protection for intellectual property such as patents, trademarks, and copyrights."
    elif message == "What does Section 141 of the Negotiable Instruments Act deal with?":
        return "Section 141 deals with the liability of companies and their directors for offenses related to dishonor of cheques."
    elif message == "What is the role of the High Courts in India?":
        return "High Courts are the principal courts of civil and criminal jurisdiction in each state, and they also handle appeals from lower courts."
    elif message == "What is Section 23 of the IPC about?":
        return "Section 23 deals with the definition of a criminal conspiracy and the punishment for engaging in such conspiracy."
    elif message == "What is the Law of Torts?":
        return "The Law of Torts deals with civil wrongs and provides remedies to individuals harmed by the wrongful acts of others."
    elif message == "What does the Arbitration and Conciliation Act cover?":
        return "This Act provides a framework for the resolution of disputes through arbitration and conciliation processes."
    elif message == "What is Section 139A of the Negotiable Instruments Act?":
        return "Section 139A deals with the presumption of liability in the case of dishonor of cheques."
    elif message == "What is the purpose of the Civil Rights Act?":
        return "The Civil Rights Act aims to prevent discrimination and ensure equal rights for all citizens."
    elif message == "What does the Public Interest Litigation (PIL) entail?":
        return "PIL allows individuals or groups to file lawsuits on behalf of the public interest or for social justice issues."
    elif message == "What is Section 304B of the IPC?":
        return "Section 304B deals with dowry death, providing punishment for the husband or his relatives if a woman dies under suspicious circumstances related to dowry demands."
    elif message == "What is the Indian Succession Act?":
        return "The Indian Succession Act provides the legal framework for inheritance and the distribution of a deceased person’s estate."
    elif message == "What is the role of the National Company Law Tribunal (NCLT)?":
        return "The NCLT adjudicates issues related to company law, including insolvency and corporate disputes."
    elif message == "What is the Civil Procedure Code (CPC) Section 25?":
        return "Section 25 allows the Supreme Court to transfer cases from one High Court to another or from a lower court to a High Court."
    elif "weather" in message:
        return "I can't check the weather right now, but you can check a weather app for current conditions."
    elif "joke" in message:
        return "Why don't scientists trust atoms? Because they make up everything!"
    else:
        return "I'm not sure how to respond to that. Can you please ask something else?"
    # Define a knowledge base (you can extend this with more detailed information)
'''def generate_response(message):
    message = message.lower().strip()

    knowledge_base={
    
        "What is Article 21 of the Indian Constitution?": "Article 21 guarantees the protection of life and personal liberty. It states that no person shall be deprived of his life or personal liberty except according to the procedure established by law.",
        "What is Section 302 of the Indian Penal Code?": "Section 302 of the IPC deals with punishment for murder. It prescribes the death penalty or life imprisonment and a fine for those convicted of murder.",
        "Can you explain Section 420 of the IPC?": "Section 420 of the IPC addresses cheating and dishonestly inducing delivery of property. It prescribes punishment for those involved in fraudulent activities.",
        "What is the Juvenile Justice Act?": "The Juvenile Justice Act deals with the care, protection, and rehabilitation of children in conflict with the law and those in need of care and protection.",
        "What does Section 498A of the IPC cover?": "Section 498A deals with the harassment of a married woman by her husband or his relatives, which includes cruelty and demands for dowry.",
        "What is the purpose of the RTI Act?": "The Right to Information (RTI) Act empowers citizens to request information from public authorities, promoting transparency and accountability in governance.",
        "What does the Indian Contract Act regulate?": "The Indian Contract Act governs the formation, performance, and enforcement of contracts in India.",
        "What is Section 377 of the IPC?": "Section 377 of the IPC was historically used to criminalize unnatural sexual offenses. It was partially decriminalized by the Supreme Court in 2018.",
        "What is the Protection of Human Rights Act?": "The Protection of Human Rights Act established the National Human Rights Commission (NHRC) to investigate human rights violations and ensure protection.",
        "What does Section 12 of the CrPC relate to?": "Section 12 of the Criminal Procedure Code (CrPC) allows the police to arrest without a warrant in certain cases where it is deemed necessary.",
        "What is the Companies Act?": "The Companies Act regulates the formation, operation, and dissolution of companies in India.",
        "What does the Consumer Protection Act aim to do?": "The Consumer Protection Act aims to safeguard consumers' rights and address grievances against unfair trade practices.",
        "What is Section 125 of the CrPC?": "Section 125 of the CrPC provides for maintenance to be given by a person to his wife, children, or parents if they are unable to maintain themselves.",
        "Can you explain the Insolvency and Bankruptcy Code?": "The Insolvency and Bankruptcy Code provides a legal framework for insolvency resolution and bankruptcy proceedings for individuals and companies.",
        "What is the Intellectual Property Rights Act?": "This Act provides protection for intellectual property such as patents, trademarks, and copyrights.",
        "What does Section 141 of the Negotiable Instruments Act deal with?": "Section 141 deals with the liability of companies and their directors for offenses related to dishonor of cheques.",
        "What is the role of the High Courts in India?": "High Courts are the principal courts of civil and criminal jurisdiction in each state, and they also handle appeals from lower courts.",
        "What is Section 23 of the IPC about?": "Section 23 deals with the definition of a criminal conspiracy and the punishment for engaging in such conspiracy.",
        "What is the Law of Torts?": "The Law of Torts deals with civil wrongs and provides remedies to individuals harmed by the wrongful acts of others.",
        "What does the Arbitration and Conciliation Act cover?": "This Act provides a framework for the resolution of disputes through arbitration and conciliation processes.",
        "What is Section 139A of the Negotiable Instruments Act?": "Section 139A deals with the presumption of liability in the case of dishonor of cheques.",
        "What is the purpose of the Civil Rights Act?": "The Civil Rights Act aims to prevent discrimination and ensure equal rights for all citizens.",
        "What does the Public Interest Litigation (PIL) entail?": "PIL allows individuals or groups to file lawsuits on behalf of the public interest or for social justice issues.",
        "What is Section 304B of the IPC?": "Section 304B deals with dowry death, providing punishment for the husband or his relatives if a woman dies under suspicious circumstances related to dowry demands.",
        "What is the Indian Succession Act?": "The Indian Succession Act provides the legal framework for inheritance and the distribution of a deceased person’s estate.",
        "What is the role of the National Company Law Tribunal (NCLT)?": "The NCLT adjudicates issues related to company law, including insolvency and corporate disputes.",
        "What is the Civil Procedure Code (CPC) Section 25?": "Section 25 allows the Supreme Court to transfer cases from one High Court to another or from a lower court to a High Court.",
        "What does Section 27 of the IPC deal with?": "Section 27 covers the punishment for the wrongful confinement of a person.",
        "What is the legal age for marriage in India?": "The legal age for marriage is 21 years for males and 18 years for females, as per the Prohibition of Child Marriage Act.",
        "What does the Transfer of Property Act Section 54 cover?": "Section 54 defines the term 'sale' of immovable property and the requirements for its transfer.",
        "What is the role of the Lok Sabha and Rajya Sabha in legislation?": "The Lok Sabha and Rajya Sabha are the two houses of Parliament responsible for making and passing laws in India.",
        "What is Section 294 of the IPC about?": "Section 294 deals with the punishment for obscene acts or songs in public places.",
        "What is the Consumer Protection Act Section 12?": "Section 12 provides the procedure for filing a complaint with the Consumer Forum.",
        "What is the aim of the National Food Security Act?": "The Act aims to provide subsidized food grains to eligible families to ensure food security.",
        "What is Section 80 of the CrPC?": "Section 80 deals with the requirement for prior notice before a person is arrested.",
        "What is the legal provision for adoption in India?": "Adoption in India is governed by the Adoption Laws (Hindu Adoption and Maintenance Act, 1956, and the Juvenile Justice Act for non-Hindus).",
        "What does Section 354 of the IPC cover?": "Section 354 deals with the punishment for assault or criminal force with the intent to outrage a woman's modesty.",
        "What is the role of the National Human Rights Commission (NHRC)?": "The NHRC investigates human rights violations and works to ensure the protection and promotion of human rights.",
        "What is Section 125 of the IPC?": "Section 125 deals with the liability for receiving stolen property and the punishment for those involved.",
        "What is the aim of the Right to Education Act?": "The Right to Education Act mandates free and compulsory education for children aged 6 to 14 years.",
        "What does Section 377A of the IPC entail?": "Section 377A deals with the criminalization of consensual homosexual acts; however, the section was decriminalized by the Supreme Court in 2018.",
        "What does Section 498A of the Indian Penal Code cover?":"Section 498A of the IPC deals with the harassment of a married woman by her husband or his relatives. It addresses cruelty and demands for dowry and provides for punishment of the offenders.",
        "What is the Protection of Women from Domestic Violence Act, 2005?": "The Protection of Women from Domestic Violence Act, 2005 provides legal protection to women who are victims of domestic violence. It offers measures such as protection orders, residence orders, and monetary relief.",
        "What does Section 354 of the IPC cover?": "Section 354 of the IPC deals with the punishment for assault or criminal force with the intent to outrage a woman's modesty. It criminalizes acts like physical assault and harassment aimed at a woman.",
        "What is the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013?": "This Act aims to protect women from sexual harassment at their workplaces. It mandates the creation of internal complaints committees and provides a mechanism for redressal and action against offenders.",
        "What is the Criminal Law (Amendment) Act, 2013?": "The Criminal Law (Amendment) Act, 2013 was enacted to address sexual offenses and improve the legal provisions for the safety of women. It includes provisions for more stringent punishment for crimes like rape and acid attacks.",
        "What does Section 376 of the IPC cover?": "Section 376 of the IPC addresses the punishment for rape. It specifies various forms of sexual assault and prescribes severe penalties for those convicted of the crime.",
        "What is the role of the National Commission for Women (NCW)?": "The National Commission for Women (NCW) is a statutory body responsible for safeguarding women's rights and addressing their grievances. It works on policy recommendations and enforcement of laws related to women's safety and empowerment.",
        "What is the purpose of the Dowry Prohibition Act, 1961?": "The Dowry Prohibition Act, 1961 prohibits the giving or receiving of dowry. It aims to prevent dowry-related harassment and violence and provides penalties for those involved in dowry transactions.",
        "What does the POCSO Act stand for and what does it cover?": "The Protection of Children from Sexual Offences (POCSO) Act, 2012 is designed to protect children from sexual offenses. It provides for the establishment of special courts and procedures for dealing with sexual abuse cases involving minors.",
        "What are the legal provisions under the Criminal Procedure Code (CrPC) for protecting women?": "The Criminal Procedure Code (CrPC) includes provisions such as Section 125 for maintenance of wives and children, and Section 498A for domestic violence. It also includes procedures for providing protection and relief to women victims of various crimes.",
        "What is the aim of the Nirbhaya Fund?": "The Nirbhaya Fund was created to enhance the safety and security of women in India. It provides financial assistance to support initiatives and projects aimed at addressing women's safety and improving their conditions.",
        "What is the objective of the National Policy for the Empowerment of Women, 2001?": "The National Policy for the Empowerment of Women, 2001 aims to create an environment where women can exercise their rights and freedoms fully. It focuses on eliminating gender-based discrimination and promoting women's empowerment.",
        "What is Section 376A of the IPC?": "Section 376A of the IPC deals with the punishment for causing death or a persistent vegetative state due to sexual assault. It prescribes life imprisonment and a fine for such offenses.",
        "What are the legal protections under the Maternity Benefit Act, 1961?": "The Maternity Benefit Act, 1961 provides for paid maternity leave and other benefits to women working in organizations. It aims to protect the health of both the mother and the child during maternity.",
        "What does the Domestic Violence (Prevention and Protection) Act, 2015 address?": "The Domestic Violence (Prevention and Protection) Act, 2015 provides a legal framework for preventing domestic violence and protecting victims. It includes measures for protection, compensation, and legal aid for victims.",
        "What is the objective of the Juvenile Justice (Care and Protection of Children) Act, 2015?": "The Juvenile Justice (Care and Protection of Children) Act, 2015 focuses on the care, protection, and rehabilitation of children, including those involved in criminal activities. It aims to ensure justice and protection for children in conflict with the law.",
        "What are the provisions of the Code of Criminal Procedure (CrPC) Section 164?": "Section 164 of the CrPC deals with the recording of statements and confessions by a police officer or magistrate. It ensures that statements made are voluntary and can be used as evidence in court.",
        "What is the aim of the Anti-Trafficking Bill, 2021?": "The Anti-Trafficking Bill, 2021 aims to prevent trafficking of persons, especially women and children. It provides for a legal framework to combat trafficking and offers protection and rehabilitation services to victims.",
        "What does the Prohibition of Child Marriage Act, 2006 cover?": "The Prohibition of Child Marriage Act, 2006 seeks to prevent child marriages by setting the legal age of marriage at 18 years for women and 21 years for men. It provides penalties for those who engage in or facilitate child marriages.",
        "What is Section 509 of the IPC?": "Section 509 of the IPC deals with the punishment for insulting the modesty of a woman through spoken words, gestures, or other means. It criminalizes acts that offend or insult a woman's dignity."

        # Add more FAQs here
    }'''
    # if message in knowledge_base:
    #     return knowledge_base[message]
    
    # Check for predefined responses
        
    
    # for question, answer in knowledge_base.items():
    #     result = nlp(question=message, context=answer)
    #     if result['score'] > 0.5:  # Adjust threshold based on needs
    #         return answer
    
# Simple rule-based responses# Other Common Queries
    
    
if __name__=="__main__":
  db.create_all()
  app.run(debug=True)