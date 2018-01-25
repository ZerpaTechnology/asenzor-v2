function type(v){}
	aType=typeof(v)
	if aType=="object"{
		if "__class__" in Object.keys(v):
			return v.__class__
		else if("__init__" in Object.keys(v)){
			return "<type 'classobj'>"

		}
		else{
			return "<type 'dict'>"
		}
		
	}
	else if(aType=="function"){
		
		if("__init__" in Object.keys(v)){
			return "<type 'classobj'>"

		}
		else{
			return "<type 'function'>"
		}		

    else {
            return (    // Odly, the braces are required here
                aType == 'boolean' ? bool :
                aType == 'string' ? str :
                aType == 'number' ? (anObject % 1 == 0 ? int : float) :
                null
            );
        }
    }
