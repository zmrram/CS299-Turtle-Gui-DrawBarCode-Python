import urllib.request
import turtle

def drawxAxis(t,x):
    t.speed(10)
    for i in range(0,x,10):
        if i % 10 == 0:
            strs = " "
            strs = strs + str(i)
            t.write(strs)
            
        t.left(90)
        t.forward(10 * 1.5)
        t.right(90)
    
def drawBar(t, height, mag):
    mag = round(mag,1)
    strs = " "
    strs = strs + str(mag)
    t.write(strs)
    t.left(90)           
    t.forward(height * 1.5)       
    if height > 0:
        strs = " "
        strs = strs + str(height)
        t.write(strs)
    t.right(90)
    t.forward(20)       
    t.right(90)
    t.forward(height * 1.5)      
    t.left(90)             
    
def main():
    #Region: Worldwide
    #Timeline: 3 months
    #Magnitute range: 1-8.5, the sever only allow ~20,000 search result.
    page =urllib.request.urlopen("http://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=2016-7-31%2000:00:00&endtime=2016-10-31%2023:59:59&minmagnitude=1&orderby=time")
    pageText = page.readline();
    dataList = []

    for i in range (0,5560):
        pageText = page.readline();
        decodedPageText = pageText.decode("utf-8")
        data = decodedPageText.split(",")
        mag = float(data[4])
        dataList.append(round(mag,1))        
    counter = []
    for i in range(0,100):
        counter.append(0)
        
    for i in range(0,100):
        for each in dataList:
            if (round(i * 0.1,1)) == each:
                counter[i] = counter[i] + 1    
    a = turtle.Turtle()
    a.penup()
    a.goto(-850, -450)
    a.pendown()
    drawxAxis(a, 600)
    a.penup()
    a.goto(-800, -450)
    a.pendown()
    x = 1
    for i in range(10,95):
        drawBar(a, counter[i],x)
        x += 0.1
        
if  __name__ =='__main__':
    main()
