import datetime

def report(info,activity):
    """
        **Report**
        This Module Generate the Report 
    """
    time = datetime.datetime.now()
    report = "Activity [ "+activity+" ]"+"\n"+info+"\n"+"Report Generated At: "+time

    return report