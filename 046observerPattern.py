class Subject:
    def __init__(self):
        self.__observers = []
    
    def attach(self, observer):
        self.__observers.append(observer)
        print(f'New observer: {observer}, total observers: {len(self.__observers)}')
        
    def detach(self, observer):
        self.__observers.remove(observer)
        
    def notify(self, *args, **kwargs):
        for observer in self.__observers:
            observer.update(self, *args, **kwargs)
    ## Subject internal state should be changed via methods that call notify on changes
            
class Observer:
    def update(self, subject, *args, **kwargs):
        print(f'update() {self} was called by: {subject}', args, kwargs)
        

somethingObservable = Subject()
someObserver = Observer()
somethingObservable.attach(someObserver)

somethingObservable.notify()
somethingObservable.notify('second update')
somethingObservable.notify('and another one update')

somethingObservable.detach(someObserver)
somethingObservable.notify('no one will hear this')

somethingObservable.attach(someObserver)
somethingObservable.notify('hello again')

secondObserver = Observer()
somethingObservable.attach(secondObserver)
somethingObservable.notify('two observers will get this')