import matplotlib.pyplot as plt

def lines():
    x1 = [1, 3, 6, 10, 23, 30, 37, 43]
    y2 = [1, 3, 6, 10, 23, 30, 37, 43]
    x2 = [3, 6, 7, 8, 9, 12, 23, 45]
    y1 = [3, 6, 7, 8, 9, 12, 23, 45]

    plt.plot(x1, y1, marker='o', markerfacecolor='blue', markersize= 8 ,label = "First pair")
    plt.plot(x2, y2, marker='x', markerfacecolor='red', markersize= 8 ,label = "Second pair")
    plt.ylim(0, 50)
    plt.xlim(0, 50)

    plt.xlabel("some intergers")
    plt.ylabel("some other intergers")

    plt.title("The G.R.A.P.H.")
    plt.legend()
    plt.show()

def bars():
    x = [1,2,3,4,5,6,7,8]
    h1 = [1, 3, 6, 10, 23, 30, 37, 43]
    barlabels = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth"]
    
    plt.bar(x, h1, tick_label= barlabels, color=["blue", "red"])

    plt.xlabel("some intergers")
    plt.ylabel("some other intergers")

    plt.title("The B.A.R. G.R.A.P.H.")
    plt.legend()
    plt.show()

lines()
bars()