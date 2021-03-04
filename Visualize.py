import json 
import plotly.graph_objects as go
import collections
import gensim

class Read:
    """
    Class to read any generic file
    
    """
    ##TODO add more file types
    def __init__(self):
        return None
    def read_json(self, filename):
        file_ = open(filename,'r')
        data = json.load(file_)
        file_.close()
        return data


class Visualize:
    """
    Class to use various plotly functions

    """
    ##TODO add more plot types to do NLP visualizations

    def __init__(self):
        return None

    def histogram(self, data,title_x, title_y,plot_title,legend,**args):
        fig = go.Figure(data=[go.Histogram(x=data)])
        fig.update_layout(
            title=plot_title,
            xaxis_title=title_x,
            yaxis_title=title_y,
            legend_title=legend,
            font=dict(
                family="Times New Roman",size=18,
                color='black'),
                xaxis={'categoryorder':'category ascending'})
        return fig


    def bar(self, datax,datay, title_x, title_y,plot_title,legend,**args):
        colors = ['aliceblue',  'aqua', 'aquamarine', 'darkturquoise']
        fig = go.Figure(go.Bar(x=datax,y=datay,orientation='h',marker={'color': datax,
                                               'colorscale': 'rainbow'}))##marker_color='darkred'))
        fig.update_layout(
            title=plot_title,
            xaxis_title=title_x,
            yaxis_title=title_y,
            legend_title=legend,
            font=dict(
                family="Times New Roman",size=18,
                color='black'),
                xaxis={'categoryorder':'category ascending'}
                
                ,yaxis=dict(autorange='reversed'))
        return fig

if __name__ =='__main__':    
    Data = Read()
    data = Data.read_json(r'432021/ABC_news.json') 
    plot = Visualize()
    All_figures=[]
    Corpus = []
    for key, value in data.items():
        if value is not None:
            
            
            temp_2 = "".join(value).replace('"','').replace('\'','').replace(',','').replace('.',' ').replace('--','').replace('———',' ').lower()
            temp_2 = gensim.parsing.preprocessing.remove_stopwords(temp_2).upper()
            Article = (temp_2.split())
            Corpus.append(temp_2)

            #print("This is the article {}".format(Article))
            counts = (collections.Counter(Article).most_common(10))
            #print(counts)
            y =[]
            x=[]
            for items in counts:
                y.append(items[0])
                x.append(items[1])
            #print(x,y)
    
        
        All_figures.append(plot.bar(x,y,'Counts','Words','Word Counts','Legend'))
    (All_figures[20]).show()
data = (collections.Counter(Corpus).most_common(10))

for items in data:
    y.append(items[0])
    x.append(items[1])
    print(y,x)
    #plot.bar(x,y,'Counts','Words','Word Counts','Legend').show()
    