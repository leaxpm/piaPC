import datetime

def report(info,activity):
    """
        **Report**
        This Module Generate the Report 
    """
    time = datetime.datetime.now()
    report = "Activity [ "+str(activity)+" ]"+"\n"+str(info)+"\n"+"Report Generated At: "+str(time)

    return report