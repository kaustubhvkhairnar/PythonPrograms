from sklearn import tree;

def MachineLearn(weight,surface):
    BallsFeatures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]];

    Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2];

    clf = tree.DecisionTreeClassifier();

    clf = clf.fit(BallsFeatures,Names);

    result = clf.predict([[weight,surface]]);

    if result == 1:
        print("Your Object looks like Tennis Ball.");
    elif result == 2:
        print("Your Object looks like Cricket Ball.");
        
def main():
    weight = int(input("Enter weight : "));
    
    surface = input("Enter Surface type of object : ");
    
    if surface.lower() == "rough":
        surface = 1;
    elif surface.lower() == "smooth":
        surface = 0;
    else:
        print("Wrong Input");
        exit();
        
    MachineLearn(weight,surface);
    
if __name__ == "__main__":
    main();
