from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone

def cross_val_score(model, n_splits, train_data, train_labels):
    skfolds = StratifiedKFold(n_splits = 3, random_state=42)

    for train_index, test_index in skfolds.split(train_data, train_labels):
        clone_clf = clone(model)
        X_train_folds = train_data[train_index]
        y_train_folds = train_labels[train_index]
        X_test_fold = train_data[test_index]
        y_test_fold = train_labels[test_index]

        clone_clf.fit(X_train_folds, y_train_folds)
        pred = clone_clf.predict(X_test_fold)
        n_correct = sum(pred == y_test_fold)
        accuracy = n_correct/len(pred)
        print(accuracy)

    

    