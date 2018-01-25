


def py_typeof(anObject):
    __pragma__("js","{}","""
    var aType = typeof anObject;
    if (aType == 'object') {    // Directly trying '__class__ in anObject' turns out to wreck anObject in Chrome if its a primitive
        try {
            
            
            if(Object.keys(anObject).indexOf("__class__") >= 0 && anObject.__class__!=null){
                return anObject.__class__;
            }
            else{
                return object;
            }

            return dict;
        }
        catch (exception) {
            console.log(exception);
            return aType;
        }
    }
    else {
        return (    // Odly, the braces are required here
            aType == 'boolean' ? bool :
            aType == 'string' ? str :
            aType == 'number' ? (anObject % 1 == 0 ? int : float) :
            null
        );
    }
    
    """)


def list(iterable):   
    if iterable.__class__!=None and iterable.__class__.__name__ =="list":
        return iterable
    __pragma__("js","{}","""

    if (typeof(iterable)=="object"){
        return Object.keys(iterable);
    }
    else{
        var instance = iterable ? [] .slice.apply (iterable) : [];  // Spread iterable, n.b. array.slice (), so array before dot
        // Sort is the normal JavaScript sort, Python sort is a non-member function
        return instance;
    }

    """)



def copy(objeto):
            if "__class__" in dir(objeto):
                if objeto.prototype!=None: 
                    
                    o=__new__(objeto.prototype.constructor)
                    for elem in dir(o):
                        if __pragma__("js","{}"," typeof getattr(o,elem)!='function'"):
                            setattr(o,elem,copy(getattr(objeto,elem)))
                    
                else:
                    
                    if __pragma__("js","{}","objeto.__proto__.constructor==Array"):
                        l=[]
                        for elem in objeto:
                            l.append(copy(elem))
                        o=Object.assign([],l)
                    elif objeto==None:
                        o=objeto
                    elif __pragma__("js","{}","objeto.__proto__.constructor==String") or __pragma__("js","{}","objeto.__proto__.constructor==Number") or __pragma__("js","{}","objeto.__proto__.constructor==Boolean"):
                        o=objeto
                    elif __pragma__("js","{}","objeto.__proto__.constructor==Function") :
                        o=objeto.prototype.constructor
                    else:
                        
                        d={}
                        for elem in objeto:
                            
                            d[elem]=copy(objeto[elem])              
                        o=Object.assign({},d)


            else:
                if type(objeto)==str or type(objeto)==int or type(objeto)==float or type(objeto)==bool:
                    
                    o=objeto.valueOf()
                elif type(objeto)!=str and type(objeto)!=int and type(objeto)!=float and type(objeto)!=bool and type(objeto)!=None:
                    o=objeto
                
                else:
                    o=objeto

            return o