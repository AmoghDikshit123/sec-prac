from sklearn.linear_model import LogisticRegression
import joblib
X=[[1],[2],[3],[4]]
y=[0,1,0,1]
model=LogisticRegression().fit(X,y)
joblib.dump(model,'model.joblib')