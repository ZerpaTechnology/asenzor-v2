var $B = __BRYTHON__;
eval(__BRYTHON__.InjectBuiltins());

var $locals___main__=$B.imported["__main__"] || {}, $locals=$locals___main__;
$locals___main__["__doc__"]=None;
$locals___main__["__name__"]=$locals___main__["__name__"] || "__main__";
$locals___main__["__file__"]="undefined";None;

var $top_frame = ["__main__", $locals___main__, "__main__", $locals___main__, "a"]; $B.frames_stack.push($top_frame); var $stack_length = $B.frames_stack.length;
try{
    ;$locals.$line_info="1,__main__";
    $B.$import("browser",["$$document","$$alert","$$window"], {}, {}, true);
$locals["$$document"]=$B.imported["browser"]["$$document"];
$locals["$$alert"]=$B.imported["browser"]["$$alert"];
$locals["$$window"]=$B.imported["browser"]["$$window"];
None;;
    ;$locals.$line_info="2,__main__";
    $B.$import("time", [],{},$locals___main__, true);None;;
    ;$locals.$line_info="3,__main__";
    $locals___main__["s"]=getattr($locals___main__["$$window"],"s");
    ;$locals.$line_info="5,__main__";
    $locals___main__["l"]=$B.$list([]);
    ;$locals.$line_info="6,__main__";
    $locals["$next719"]=getattr($B.$iter(getattr(getattr($locals___main__["$$document"],"get"),"__call__")({$nat:"kw",kw:{selector:".menu"}})),"__next__")
    if(isinstance(getattr(getattr($locals___main__["$$document"],"get"),"__call__")({$nat:"kw",kw:{selector:".menu"}}), dict)){$locals.$len_func719=getattr(getattr(getattr($locals___main__["$$document"],"get"),"__call__")({$nat:"kw",kw:{selector:".menu"}}),"__len__"); $locals.$len719=$locals.$len_func719()}else{$locals.$len719=null}
    ;$locals.$line_info="6,__main__";
    while(1){
        if($locals.$len719!==null && $locals.$len719!=$locals.$len_func719()){throw RuntimeError("dictionary changed size during iteration")}
        try{
            $locals___main__["elem"]=$locals["$next719"]();
        }
        catch($err){if($B.is_exc($err,[StopIteration])){$B.clear_exc();break;}else{throw($err)}}
        ;$locals.$line_info="7,__main__";
        getattr(getattr($locals___main__["l"],"append"),"__call__")(getattr($locals___main__["elem"],"text"));
        $locals.$line_info="6,__main__";
    }
    ;$locals.$line_info="8,__main__";
    $locals___main__["change"] = (function ($defaults){function change720(evt){
        var $locals___main___change_270={}, $local_name="__main___change_270",$locals=$locals___main___change_270;
        ;var $top_frame = [$local_name, $locals,"__main__", $locals___main__]; $B.frames_stack.push($top_frame); var $stack_length = $B.frames_stack.length;
        try{
            var $len = arguments.length;
            if($len>0 && arguments[$len-1].$nat!==undefined){
                $locals___main___change_270 = $locals = $B.args("change", 1, {evt:null}, ["evt"], arguments, {}, null, null);
            }
            else{
                if($len!=1){$B.wrong_nb_args("change", $len, 1, ["evt"])}
                $locals___main___change_270=$locals={evt:evt}
            }
            $B.frames_stack[$B.frames_stack.length-1][1] = $locals;
            $B.js_this = this;
            ;$locals.$line_info="9,__main__";
            getattr(getattr($locals["evt"],"preventDefault"),"__call__")();
            ;$locals.$line_info="10,__main__";
            var $failed728=false;
                try{
                ;$locals.$line_info="11,__main__";
                if($B.$bool($B.rich_comp("__eq__",$B.builtins.str(getattr($locals["evt"],"target")),"<HTMLSpanElement object>"))){
                    ;$locals.$line_info="12,__main__";
                    $locals["$next721"]=getattr($B.$iter(getattr($locals___main__["s"](".menu"),"iterables")),"__next__")
                    if(isinstance(getattr($locals___main__["s"](".menu"),"iterables"), dict)){$locals.$len_func721=getattr(getattr($locals___main__["s"](".menu"),"iterables"),"__len__"); $locals.$len721=$locals.$len_func721()}else{$locals.$len721=null}
                    ;$locals.$line_info="12,__main__";
                    while(1){
                        if($locals.$len721!==null && $locals.$len721!=$locals.$len_func721()){throw RuntimeError("dictionary changed size during iteration")}
                        try{
                            $locals["elem"]=$locals["$next721"]();
                        }
                        catch($err){if($B.is_exc($err,[StopIteration])){$B.clear_exc();break;}else{throw($err)}}
                        ;$locals.$line_info="13,__main__";
                        if($B.$bool($B.rich_comp("__eq__",$B.$getitem(getattr($locals["elem"],"children"),0),getattr($locals["evt"],"target")))){
                            ;$locals.$line_info="15,__main__";
                            getattr(getattr($locals___main__["s"](getattr(getattr($locals["evt"],"target"),"parent")),"addClass"),"__call__")("bg-bluelight");
                        }
                        else{
                            ;$locals.$line_info="20,__main__";
                            getattr(getattr($locals___main__["s"](getattr($locals["elem"],"parent")),"removeClass"),"__call__")("bg-bluelight");
                            ;$locals.$line_info="21,__main__";
                            getattr(getattr($locals___main__["s"]($locals["elem"]),"removeClass"),"__call__")("bg-bluelight");
                        }
                        $locals.$line_info="12,__main__";
                    }
                }
                else{
                    ;$locals.$line_info="23,__main__";
                    $locals["$next722"]=getattr($B.$iter(getattr($locals___main__["s"](".menu"),"iterables")),"__next__")
                    if(isinstance(getattr($locals___main__["s"](".menu"),"iterables"), dict)){$locals.$len_func722=getattr(getattr($locals___main__["s"](".menu"),"iterables"),"__len__"); $locals.$len722=$locals.$len_func722()}else{$locals.$len722=null}
                    ;$locals.$line_info="23,__main__";
                    while(1){
                        if($locals.$len722!==null && $locals.$len722!=$locals.$len_func722()){throw RuntimeError("dictionary changed size during iteration")}
                        try{
                            $locals["elem"]=$locals["$next722"]();
                        }
                        catch($err){if($B.is_exc($err,[StopIteration])){$B.clear_exc();break;}else{throw($err)}}
                        ;$locals.$line_info="24,__main__";
                        if($B.$bool($B.rich_comp("__eq__",$locals["elem"],getattr($locals["evt"],"target")))){
                            ;$locals.$line_info="27,__main__";
                            getattr(getattr($locals___main__["s"](getattr($locals["evt"],"target")),"addClass"),"__call__")("bg-bluelight");
                        }
                        else{
                            ;$locals.$line_info="30,__main__";
                            getattr(getattr($locals___main__["s"](getattr($locals["elem"],"parent")),"removeClass"),"__call__")("bg-bluelight");
                            ;$locals.$line_info="31,__main__";
                            getattr(getattr($locals___main__["s"]($locals["elem"]),"removeClass"),"__call__")("bg-bluelight");
                        }
                        $locals.$line_info="23,__main__";
                    }
                }
                ;$locals.$line_info="34,__main__";
                $locals["indice"]=getattr(getattr($locals___main__["l"],"index"),"__call__")(getattr(getattr($locals["evt"],"target"),"text"));
                ;$locals.$line_info="35,__main__";
                $locals["subs"]=getattr(getattr($locals___main__["$$document"],"get"),"__call__")({$nat:"kw",kw:{selector:".sub"}});
                ;$locals.$line_info="37,__main__";
                if($B.$bool($B.$is_member("hidden",getattr($B.$getitem($locals["subs"],$locals["indice"]),"class_name")))){
                    ;$locals.$line_info="38,__main__";
                    $locals["$next723"]=getattr($B.$iter($locals["subs"]),"__next__")
                    if(isinstance($locals["subs"], dict)){$locals.$len_func723=getattr($locals["subs"],"__len__"); $locals.$len723=$locals.$len_func723()}else{$locals.$len723=null}
                    ;$locals.$line_info="38,__main__";
                    while(1){
                        if($locals.$len723!==null && $locals.$len723!=$locals.$len_func723()){throw RuntimeError("dictionary changed size during iteration")}
                        try{
                            $locals["elem"]=$locals["$next723"]();
                        }
                        catch($err){if($B.is_exc($err,[StopIteration])){$B.clear_exc();break;}else{throw($err)}}
                        ;$locals.$line_info="39,__main__";
                        if($B.$bool(!$B.$is_member("hidden",getattr($locals["elem"],"class_name")))){
                            ;$locals.$line_info="40,__main__";
                            var $temp,$left;
                            $temp=" hidden";
                            if(!hasattr(getattr($locals["elem"],"class_name"),"__iadd__")){
                                setattr($locals["elem"],"class_name",getattr(getattr($locals["elem"],"class_name"), "__add__")($temp));None;;
                            }
                            else{
                                getattr(getattr($locals["elem"],"class_name"),"__iadd__")($temp)
                            }
                        }
                        $locals.$line_info="38,__main__";
                    }
                    ;$locals.$line_info="41,__main__";
                    setattr($B.$getitem($locals["subs"],$locals["indice"]),"class_name",getattr(getattr(getattr($B.$getitem($locals["subs"],$locals["indice"]),"class_name"),"replace"),"__call__")("hidden", ""));None;;
                }
                else{
                    ;$locals.$line_info="47,__main__";
                    var $temp,$left;
                    $temp=" hidden";
                    if(!hasattr(getattr($B.$getitem($locals["subs"],$locals["indice"]),"class_name"),"__iadd__")){
                        setattr($B.$getitem($locals["subs"],$locals["indice"]),"class_name",getattr(getattr($B.$getitem($locals["subs"],$locals["indice"]),"class_name"), "__add__")($temp));None;;
                    }
                    else{
                        getattr(getattr($B.$getitem($locals["subs"],$locals["indice"]),"class_name"),"__iadd__")($temp)
                    }
                }
            }
            catch($err728){
                var $failed728=true;$B.pmframe=$B.last($B.frames_stack);if(0){}
                else if(($locals.$line_info="50,__main___change_270") && $B.is_exc($err728,[$B.builtins.Exception])){
                    $locals["e"]=$B.exception($err728)
                    ;$locals.$line_info="51,__main__";
                    getattr($locals___main__["$$alert"],"__call__")($locals["e"]);
                    ;$locals.$line_info="52,__main__";
                    getattr($locals___main__["$$alert"],"__call__")("===");
                }
                else{
                    throw $err728
                }
            }
            $B.leave_frame($local_name);return None
        }
        catch(err){
            $B.leave_frame($local_name);throw err
        }
    }
    change720.$infos = {
        __name__:"change",
        __defaults__ : [],
        __module__ : "__main__",
        __doc__: None,
        __annotations__: {},
        __code__:{
            __class__:$B.$CodeDict,
            co_argcount:1,
            co_filename:$locals___main__["__file__"],
            co_firstlineno:8,
            co_flags:67,
            co_kwonlyargcount:0,
            co_name: "change",
            co_nlocals: 5,
            co_varnames: ["evt", "elem", "indice", "subs", "e"]
        }
    };None;
    return change720})({})
    ;$locals.$line_info="53,__main__";
    $locals___main__["change"] = (function ($defaults){function change724(evt){
        var $locals___main___change_271={}, $local_name="__main___change_271",$locals=$locals___main___change_271;
        ;var $top_frame = [$local_name, $locals,"__main__", $locals___main__]; $B.frames_stack.push($top_frame); var $stack_length = $B.frames_stack.length;
        try{
            var $len = arguments.length;
            if($len>0 && arguments[$len-1].$nat!==undefined){
                $locals___main___change_271 = $locals = $B.args("change", 1, {evt:null}, ["evt"], arguments, {}, null, null);
            }
            else{
                if($len!=1){$B.wrong_nb_args("change", $len, 1, ["evt"])}
                $locals___main___change_271=$locals={evt:evt}
            }
            $B.frames_stack[$B.frames_stack.length-1][1] = $locals;
            $B.js_this = this;
            ;$locals.$line_info="55,__main__";
            $locals["$next725"]=getattr($B.$iter($B.builtins.enumerate(getattr(getattr($B.$getitem($locals___main__["s"]("#main-menu"),0),"get"),"__call__")({$nat:"kw",kw:{selector:"span[name='menu']"}}))),"__next__")
            if(isinstance($B.builtins.enumerate(getattr(getattr($B.$getitem($locals___main__["s"]("#main-menu"),0),"get"),"__call__")({$nat:"kw",kw:{selector:"span[name='menu']"}})), dict)){$locals.$len_func725=getattr($B.builtins.enumerate(getattr(getattr($B.$getitem($locals___main__["s"]("#main-menu"),0),"get"),"__call__")({$nat:"kw",kw:{selector:"span[name='menu']"}})),"__len__"); $locals.$len725=$locals.$len_func725()}else{$locals.$len725=null}
            ;$locals.$line_info="55,__main__";
            while(1){
                if($locals.$len725!==null && $locals.$len725!=$locals.$len_func725()){throw RuntimeError("dictionary changed size during iteration")}
                try{
                    var $right729 = getattr($B.$iter($locals["$next725"]()),"__next__");
                    var $rlist729=[], $pos=0;while(1){try{$rlist729[$pos++] = $right729()}catch(err){break}};
                    if($rlist729.length<2){throw ValueError("need more than "+$rlist729.length+" value" + ($rlist729.length>1 ? "s" : "")+" to unpack")}
                    if($rlist729.length>2){throw ValueError("too many values to unpack (expected 2)")}
                    $locals["k"]=$rlist729[0];
                    $locals["elem"]=$rlist729[1];
                }
                catch($err){if($B.is_exc($err,[StopIteration])){$B.clear_exc();break;}else{throw($err)}}
                ;$locals.$line_info="56,__main__";
                if($B.$bool($B.rich_comp("__ne__",$locals["elem"],getattr($locals["evt"],"target")))){
                    ;$locals.$line_info="57,__main__";
                    getattr(getattr($locals___main__["s"]($locals["elem"]),"removeClass"),"__call__")("bg-bluelight");
                    ;$locals.$line_info="58,__main__";
                    getattr(getattr($locals___main__["s"]($B.$getitem(getattr(getattr($locals["elem"],"parent"),"children"),1)),"addClass"),"__call__")("hidden");
                }
                else{
                    ;$locals.$line_info="60,__main__";
                    getattr(getattr($locals___main__["s"](getattr($locals["evt"],"target")),"addClass"),"__call__")("bg-bluelight");
                    ;$locals.$line_info="61,__main__";
                    getattr(getattr($locals___main__["s"]($B.$getitem(getattr(getattr(getattr($locals["evt"],"target"),"parent"),"children"),1)),"removeClass"),"__call__")("hidden");
                }
                $locals.$line_info="55,__main__";
            }
            $B.leave_frame($local_name);return None
        }
        catch(err){
            $B.leave_frame($local_name);throw err
        }
    }
    change724.$infos = {
        __name__:"change",
        __defaults__ : [],
        __module__ : "__main__",
        __doc__: None,
        __annotations__: {},
        __code__:{
            __class__:$B.$CodeDict,
            co_argcount:1,
            co_filename:$locals___main__["__file__"],
            co_firstlineno:53,
            co_flags:67,
            co_kwonlyargcount:0,
            co_name: "change",
            co_nlocals: 3,
            co_varnames: ["evt", "k", "elem"]
        }
    };None;
    return change724})({})
    ;$locals.$line_info="63,__main__";
    $locals["$next726"]=getattr($B.$iter($B.builtins.enumerate(getattr(getattr($B.$getitem($locals___main__["s"]("#main-menu"),0),"get"),"__call__")({$nat:"kw",kw:{selector:"span[name='menu']"}}))),"__next__")
    if(isinstance($B.builtins.enumerate(getattr(getattr($B.$getitem($locals___main__["s"]("#main-menu"),0),"get"),"__call__")({$nat:"kw",kw:{selector:"span[name='menu']"}})), dict)){$locals.$len_func726=getattr($B.builtins.enumerate(getattr(getattr($B.$getitem($locals___main__["s"]("#main-menu"),0),"get"),"__call__")({$nat:"kw",kw:{selector:"span[name='menu']"}})),"__len__"); $locals.$len726=$locals.$len_func726()}else{$locals.$len726=null}
    ;$locals.$line_info="63,__main__";
    while(1){
        if($locals.$len726!==null && $locals.$len726!=$locals.$len_func726()){throw RuntimeError("dictionary changed size during iteration")}
        try{
            var $right730 = getattr($B.$iter($locals["$next726"]()),"__next__");
            var $rlist730=[], $pos=0;while(1){try{$rlist730[$pos++] = $right730()}catch(err){break}};
            if($rlist730.length<2){throw ValueError("need more than "+$rlist730.length+" value" + ($rlist730.length>1 ? "s" : "")+" to unpack")}
            if($rlist730.length>2){throw ValueError("too many values to unpack (expected 2)")}
            $locals___main__["k"]=$rlist730[0];
            $locals___main__["elem"]=$rlist730[1];
        }
        catch($err){if($B.is_exc($err,[StopIteration])){$B.clear_exc();break;}else{throw($err)}}
        ;$locals.$line_info="64,__main__";
        getattr(getattr($locals___main__["elem"],"bind"),"__call__")("click", $locals___main__["change"]);
        $locals.$line_info="63,__main__";
    }
    ;$locals.$line_info="67,__main__";
    $locals___main__["change2"] = (function ($defaults){function change2727(evt){
        var $locals___main___change2_272={}, $local_name="__main___change2_272",$locals=$locals___main___change2_272;
        ;var $top_frame = [$local_name, $locals,"__main__", $locals___main__]; $B.frames_stack.push($top_frame); var $stack_length = $B.frames_stack.length;
        try{
            var $len = arguments.length;
            if($len>0 && arguments[$len-1].$nat!==undefined){
                $locals___main___change2_272 = $locals = $B.args("change2", 1, {evt:null}, ["evt"], arguments, {}, null, null);
            }
            else{
                if($len!=1){$B.wrong_nb_args("change2", $len, 1, ["evt"])}
                $locals___main___change2_272=$locals={evt:evt}
            }
            $B.frames_stack[$B.frames_stack.length-1][1] = $locals;
            $B.js_this = this;
            ;$locals.$line_info="69,__main__";
            if($B.$bool($B.$is_member("hidden",getattr($B.$getitem($locals___main__["$$document"],"menu"),"class_name")))){
                ;$locals.$line_info="70,__main__";
                setattr($B.$getitem($locals___main__["$$document"],"menu"),"class_name",getattr(getattr(getattr($B.$getitem($locals___main__["$$document"],"menu"),"class_name"),"replace"),"__call__")("hidden", ""));None;;
                ;$locals.$line_info="73,__main__";
                setattr($B.$getitem($locals___main__["$$document"],"content"),"class_name",getattr(getattr(getattr($B.$getitem($locals___main__["$$document"],"content"),"class_name"),"replace"),"__call__")("col-sm-offset-1", ""));None;;
                ;$locals.$line_info="74,__main__";
                var $temp,$left;
                $temp=" col-sm-offset-2";
                if(!hasattr(getattr($B.$getitem($locals___main__["$$document"],"content"),"class_name"),"__iadd__")){
                    setattr($B.$getitem($locals___main__["$$document"],"content"),"class_name",getattr(getattr($B.$getitem($locals___main__["$$document"],"content"),"class_name"), "__add__")($temp));None;;
                }
                else{
                    getattr(getattr($B.$getitem($locals___main__["$$document"],"content"),"class_name"),"__iadd__")($temp)
                }
            }
            else{
                ;$locals.$line_info="76,__main__";
                var $temp,$left;
                $temp=" hidden";
                if(!hasattr(getattr($B.$getitem($locals___main__["$$document"],"menu"),"class_name"),"__iadd__")){
                    setattr($B.$getitem($locals___main__["$$document"],"menu"),"class_name",getattr(getattr($B.$getitem($locals___main__["$$document"],"menu"),"class_name"), "__add__")($temp));None;;
                }
                else{
                    getattr(getattr($B.$getitem($locals___main__["$$document"],"menu"),"class_name"),"__iadd__")($temp)
                }
                ;$locals.$line_info="78,__main__";
                var $temp,$left;
                $temp=" col-sm-offset-1";
                if(!hasattr(getattr($B.$getitem($locals___main__["$$document"],"content"),"class_name"),"__iadd__")){
                    setattr($B.$getitem($locals___main__["$$document"],"content"),"class_name",getattr(getattr($B.$getitem($locals___main__["$$document"],"content"),"class_name"), "__add__")($temp));None;;
                }
                else{
                    getattr(getattr($B.$getitem($locals___main__["$$document"],"content"),"class_name"),"__iadd__")($temp)
                }
                ;$locals.$line_info="79,__main__";
                setattr($B.$getitem($locals___main__["$$document"],"content"),"class_name",getattr(getattr(getattr($B.$getitem($locals___main__["$$document"],"content"),"class_name"),"replace"),"__call__")("col-sm-offset-2", ""));None;;
            }
            $B.leave_frame($local_name);return None
        }
        catch(err){
            $B.leave_frame($local_name);throw err
        }
    }
    change2727.$infos = {
        __name__:"change2",
        __defaults__ : [],
        __module__ : "__main__",
        __doc__: None,
        __annotations__: {},
        __code__:{
            __class__:$B.$CodeDict,
            co_argcount:1,
            co_filename:$locals___main__["__file__"],
            co_firstlineno:67,
            co_flags:67,
            co_kwonlyargcount:0,
            co_name: "change2",
            co_nlocals: 1,
            co_varnames: ["evt"]
        }
    };None;
    return change2727})({})
    ;$locals.$line_info="83,__main__";
    getattr(getattr($B.$getitem($locals___main__["$$document"],"btn-menu"),"bind"),"__call__")("click", $locals___main__["change2"]);
    $B.leave_frame("__main__")
}
catch(err){
    $B.leave_frame("__main__")
    throw err
}
