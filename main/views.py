from django.shortcuts import render
from main.models import Contact,User,Feedback




def index (request): 
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        u=User(name=name,email=email,phoneno=phoneno)
        u.save()
        return render(request, 'main/project.html')
    return render(request, 'main/index.html')

def project (request): 
    return render(request, 'main/project.html')

def getPredictions(Gender,SSC,HSC,Phy,Chem,Bio,Maths,NatureWork,Literacy,Living,Finance,hrs,CreativeThink,SelfLearn,Coding,Pubskill,Comp,Extracurr,Teams,Sports,ReadWrite,Subject,HWSW,gap):
    import pickle
    model = pickle.load(open("main/CareerModel.pkl","rb"))
    prediction = model.predict([[Gender,SSC,HSC,Phy,Chem,Bio,Maths,NatureWork,Literacy,Living,Finance,hrs,CreativeThink,SelfLearn,Coding,Pubskill,Comp,Extracurr,Teams,Sports,ReadWrite,Subject,HWSW,gap]])
    y=['BBA','BDS','BE Computer Science','BE Electronics','BE Mechanical','BPharmacy','BSc Maths and Stats','BSc Computer','BSc IT','BSc Physics','MBBS']
    #y=pickle.load(open("main/RoleDF.sav","rb"))
    print(y[prediction[0]])
    return (y[prediction[0]])
result="temp"

def service (request): 
    result=None
    if request.method=="POST":
        Gender = request.POST['input1']
        SSC = request.POST['input2']
        HSC = request.POST['input3']
        Phy = request.POST['input4']
        Chem = request.POST['input5']
        Bio = request.POST['input6']
        Maths = request.POST['input7']
        NatureWork = request.POST['input8']
        Literacy = request.POST['input9']
        Living = request.POST['input10']
        Finance = request.POST['input11']
        hrs = request.POST['input12']
        CreativeThink = request.POST['input13']
        SelfLearn = request.POST['input14']
        Coding =request.POST['input15']
        Pubskill = request.POST['input16']
        Comp = request.POST['input17']
        Extracurr = request.POST['input18']
        Teams = request.POST['input19']
        Sports = request.POST['input20']
        ReadWrite =request.POST['input21']
        Subject = request.POST['input22']
        HWSW = request.POST['input23']
        gap = request.POST['input24']
        print(Gender,SSC,HSC,Phy,Chem,Bio,Maths,hrs,CreativeThink,SelfLearn,Coding,Pubskill,ReadWrite,gap)
        #result=getPredictions(Gender,SSC,HSC,Phy,Chem,Bio,Maths,NatureWork,Literacy,Living,Finance,hrs,CreativeThink,SelfLearn,Coding,Pubskill,Comp,Extracurr,Teams,Sports,ReadWrite,Subject,HWSW,gap)
        ins=Contact(Gender=Gender,SSC=SSC,HSC=HSC,Phy=Phy,Chem=Chem,Bio=Bio,Maths=Maths,NatureWork=NatureWork,Literacy=Literacy,Living=Living,Finance=Finance,hrs=hrs,CreativeThink=CreativeThink,SelfLearn=SelfLearn,Coding=Coding,Pubskill=Pubskill,Comp=Comp,Extracurr=Extracurr,Teams=Teams,Sports=Sports,ReadWrite=ReadWrite,Subject=Subject,HWSW=HWSW,gap=gap)
        ins.save() 
        import pickle
        model = pickle.load(open("main/CareerModel.pkl","rb"))
        prediction = model.predict([[Gender,SSC,HSC,Phy,Chem,Bio,Maths,NatureWork,Literacy,Living,Finance,hrs,CreativeThink,SelfLearn,Coding,Pubskill,Comp,Extracurr,Teams,Sports,ReadWrite,Subject,HWSW,gap]])
        y=['BBA','BDS','BE Computer Science','BE Electronics','BE Mechanical','BPharmacy','BSc Maths and Stats','BSc Computer','BSc IT','BSc Physics','MBBS']
        #y=pickle.load(open("main/RoleDF.sav","rb"))
        result= y[prediction[0]]
        return result
    return render(request, 'main/service.html',{'result':result})

def prediction (request): 
    result=service(request)
    print("prediction",result)
    return render(request, 'main/prediction.html',{'result':result})

def contact (request): 
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        fb=Feedback(name=name,email=email,message=message)
        fb.save()
    return render(request, 'main/contact.html')

