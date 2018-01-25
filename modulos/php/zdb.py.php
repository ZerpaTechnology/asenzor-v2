<?php
set_include_path(get_include_path() . PATH_SEPARATOR . dirname(__FILE__) . DIRECTORY_SEPARATOR . 'libpy2php');
require_once('libpy2php.php');
$email = '<type \'email\'>';

function decode($cadena) {
    $cadena = $cadena->replace('%20', ' ');
    $cadena = $cadena->replace('%7B', '{');
    $cadena = $cadena->replace('%7D', '}');
    return $cadena;
}
class obj {
    function __construct($valor,$tipo=null) {
        $this->valor = $valor;
        $this->tipo = $tipo;
    }
}
function DB($dbfile=null,$debug=false) {
    function db($tabla=null,$herencia=null,$copia=null) {
        $self = db;
        $self->t = $tabla;
        $self->error = [];
        function consola($mensaje,$d,$error=false) {
            $d->log[] = $mensaje;
            if (($d->debug == true)) {
                pyjslib_printnl($mensaje);
            }
            if ($error) {
                $d->errores[] = $mensaje;
            }
        }
        $self->consola = $consola;
        if (!in_array($tabla, $self->tablas) && !in_array($tabla, $self->campos)) {
            $self->campos[$tabla] = [];
            $self->clavePrimaria[$tabla] = 0;
            if (($herencia != null)) {
                $self->campos[$tabla] = copy::copy($self->campos[$herencia]);
            }
            $self->tablas[$tabla] = [];
            if (($copia != null)) {
                $self->tablas[$tabla] = copy::copy($self->tablas[$copia]);
                $self->clavePrimaria[$tabla] = (count($self->tablas[$tabla]) - 1);
            }
            $self->log = [];
            $self->nmodif = 0;
            $self->lrelaciones = [];
            $self->relaciones = [];
        }
        $self->seleccion = $tabla;
        $self->idseleccion = null;
        
        function dbtype($dato,$formato=null) {
            try {
                if ((type($dato) == $str)) {
                    if (('mailto:' == array_slice($dato, null, count('mailto:'))) && in_array('@', $dato) && in_array('.com', array_slice($dato, $dato->index('@'), null)) || in_array('.org', array_slice($dato, $dato->index('@'), null)) || in_array('.net', array_slice($dato, $dato->index('@'), null))) {
                        return '<type \'email\'>';
                    }
                    else if (('date:' == array_slice($dato, null, count('date:')))) {
                        if (($formato != null)) {
                            try {
                                $data = array_slice($dato, count('date:'), null);
                                $sp = $formato->replace('%d', '')->replace('%m', '')->replace('%y', '')[0];
                                if (in_array($sp, $data)) {
                                    foreach( $data->split($sp) as $elem ) {
                                        try {
                                            pyjslib_int($elem);
                                        }
                                        catch(Exception $e) {
                                                                                        return;
                                        }
                                    }
                                }
                                return '<type \'date\'>';
                            }
                            catch(Exception $e) {
                                                                pyjslib_printnl('Error en dbtype -> date');
                                pyjslib_printnl($e);
                                throw new Exception('py2php: python code would raise pre-existing exception here.');
                            }
                        }
                        else {
                            pyjslib_printnl(['Hace falta formato para ', $dato], true);
                            return;
                        }
                    }
                    else if (('datetime:' == array_slice($dato, null, count('datetime:')))) {
                        if (($formato != null)) {
                            try {
                                $data = array_slice($dato, count('datetime:'), null);
                                if (in_array(' - ', $data) && in_array(' - ', $formato) && ($formato->count(' - ') == 1)) {
                                    $parts = $data->split(' - ');
                                    $fparts = $formato->split(' - ');
                                    if (($dbtype($parts[0], $fparts[0]) == '<type \'date\'>') && ($dbtype($parts[1], $fparts[1]) == '<type \'time\'>')) {
                                        return '<type \'datetime\'>';
                                    }
                                    else if (($dbtype($parts[1], $fparts[1]) == '<type \'date\'>') && ($dbtype($parts[0], $fparts[0]) == '<type \'time\'>')) {
                                        return '<type \'datetime\'>';
                                    }
                                }
                                else if (in_array(' ', $data) && in_array(' ', $formato) && ($formato->count(' ') == 1)) {
                                    $parts = $data->split(' ');
                                    $fparts = $formato->split(' ');
                                    if (($dbtype('date:' . $parts[0], $fparts[0]) == '<type \'date\'>') && ($dbtype('time:' . $parts[1], $fparts[1]) == '<type \'time\'>')) {
                                        return '<type \'datetime\'>';
                                    }
                                    else if (($dbtype('date:' . $parts[1], $fparts[1]) == '<type \'date\'>') && ($dbtype('time:' . $parts[0], $fparts[0]) == '<type \'time\'>')) {
                                        return '<type \'datetime\'>';
                                    }
                                }
                                else {
                                    return;
                                }
                            }
                            catch(Exception $e) {
                                                                pyjslib_printnl('error en dbtype -> datetime<br>');
                                pyjslib_printnl($e);
                                throw new Exception('py2php: python code would raise pre-existing exception here.');
                            }
                        }
                        else {
                            pyjslib_printnl(['Hace falta formato para ', $dato], true);
                        }
                    }
                    else if (('time:' == array_slice($dato, null, count('time:')))) {
                        if (($formato != null)) {
                            try {
                                $data = array_slice($dato, count('time:'), null);
                                if (in_array('%H', $formato) && in_array('%M', $formato) && in_array('%S', $formato)) {
                                    $sp = $formato->replace('%H', '')->replace('%M', '')->replace('%S', '')[0];
                                    foreach( $data->split($sp) as $elem ) {
                                        try {
                                            if (($elem != '')) {
                                                pyjslib_int($elem);
                                            }
                                        }
                                        catch(Exception $e) {
                                                                                        return;
                                        }
                                    }
                                    return '<type \'time\'>';
                                }
                                else if (in_array('%H', $formato) && in_array('%M', $formato) && !in_array('%S', $formato)) {
                                    $sp = $formato->replace('%H', '')->replace('%M', '')[0];
                                    foreach( $data->split($sp) as $elem ) {
                                        try {
                                            if (($elem != '')) {
                                                pyjslib_int($elem);
                                            }
                                        }
                                        catch(Exception $e) {
                                                                                        return;
                                        }
                                    }
                                    return '<type \'time\'>';
                                }
                                else if (in_array('%I', $formato) && in_array('%M', $formato) && in_array('%S', $formato)) {
                                    $sp = $formato->replace('%I', '')->replace('%M', '')->replace('%S', '')[0];
                                    foreach( $data->split($sp) as $elem ) {
                                        try {
                                            if (($elem != '')) {
                                                pyjslib_int($elem);
                                            }
                                        }
                                        catch(Exception $e) {
                                                                                        return;
                                        }
                                    }
                                    return '<type \'time\'>';
                                }
                                else if (in_array('%I', $formato) && in_array('%M', $formato) && !in_array('%S', $formato)) {
                                    $sp = $formato->replace('%I', '')->replace('%M', '')[0];
                                    foreach( $data->split($sp) as $elem ) {
                                        try {
                                            if (($elem != '')) {
                                                pyjslib_int($elem);
                                            }
                                        }
                                        catch(Exception $e) {
                                                                                        return;
                                        }
                                    }
                                    return '<type \'time\'>';
                                }
                                else if (!in_array('%I', $formato) && !in_array('%H', $formato) && in_array('%M', $formato) && in_array('%S', $formato)) {
                                    $sp = $formato->replace('%M', '')->replace('%S', '')[0];
                                    foreach( $data->split($sp) as $elem ) {
                                        try {
                                            if (($elem != '')) {
                                                pyjslib_int($elem);
                                            }
                                        }
                                        catch(Exception $e) {
                                                                                        return;
                                        }
                                    }
                                    return '<type \'time\'>';
                                }
                                else if (!in_array('%I', $formato) && !in_array('%H', $formato) && !in_array('%M', $formato) && in_array('%S', $formato)) {
                                    try {
                                        if (($elem != '')) {
                                            pyjslib_int($data);
                                        }
                                    }
                                    catch(Exception $e) {
                                                                                return;
                                    }
                                    return '<type \'time\'>';
                                }
                                else if (!in_array('%I', $formato) && !in_array('%H', $formato) && in_array('%M', $formato) && !in_array('%S', $formato)) {
                                    try {
                                        if (($elem != '')) {
                                            pyjslib_int($data);
                                        }
                                    }
                                    catch(Exception $e) {
                                                                                return;
                                    }
                                    return '<type \'time\'>';
                                }
                                else {
                                    return;
                                }
                            }
                            catch(Exception $e) {
                                                                pyjslib_printnl('Error en dbtype -> time');
                                pyjslib_printnl($e);
                                throw new Exception('py2php: python code would raise pre-existing exception here.');
                            }
                        }
                        else {
                            pyjslib_printnl(['Hace falta formato para ', $dato], true);
                        }
                    }
                    else if (('https://' == array_slice($dato, null, count('https://'))) || ('http://' == array_slice($dato, null, count('http://'))) || ('ftp://' == array_slice($dato, null, count('ftp://') || ('news://' == array_slice($dato, null, count('news://'))))) || ('telnet://' == array_slice($dato, null, count('telnet://')))) {
                        return '<type \'url\'>';
                    }
                    else if (('data:' == array_slice($dato, null, count('data:')))) {
                        return '<type \'binary\'>';
                    }
                    else if (('password:' == array_slice($dato, null, count('password:')))) {
                        return '<type \'password\'>';
                    }
                    else if (('ldap:' == array_slice($dato, null, count('ldap:')))) {
                        return '<type \'serverFolder\'>';
                    }
                    else if (('file://' == array_slice($dato, null, count('file://')))) {
                        return '<type \'file\'>';
                    }
                    else {
                        if ((count($dato) >= 70)) {
                            return '<type \'doc\'>';
                        }
                        else {
                            return $str;
                        }
                    }
                }
                else {
                    try {
                        return $dato->tipo;
                    }
                    catch(Exception $e) {
                                                return type($dato);
                    }
                }
            }
            catch(Exception $e) {
                                pyjslib_printnl('error en dbtype <br>');
                pyjslib_printnl($e);
                throw new Exception('py2php: python code would raise pre-existing exception here.');
            }
        }
        
        function rtype($tipo) {
            $c = pyjslib_str($tipo);
            return array_slice($c, count('<type \''), -2 - count('<type \''));
        }
        function obtenerFormato($campo) {
            foreach( $self->campos[$self->seleccion] as $elem ) {
                if (($elem[0] == $campo)) {
                    return $elem[9];
                }
            }
        }
        function id($i) {
            $self->idseleccion = $i;
            return $self;
        }
        function columna($camp) {
            pyjslib_printnl($self->idseleccion);
            if (($self->t != null)) {
                $self->consola(pyjslib_str($self->tablas[$self->seleccion][$self->idseleccion][$self->obtenerCampo($camp)]) . '
', $self);
                return $self->tablas[$self->seleccion][$self->idseleccion][$self->obtenerCampo($camp)];
            }
        }
        function campo($nombre,$tipo,$unico=false,$vacio=true,$unicaFila=false,$unicacolumna=false,$mini=0,$maxi=-1,$step=null,$formato=null) {
            try {
                $self->campos[$self->seleccion][] = [$nombre, $tipo, $unico, $vacio, $unicaFila, $unicacolumna, $mini, $maxi, $step, $formato];
                if (($tabla != null)) {
                    if ((type($formato) == $str)) {
                        $formato = '\'' . $formato . '\'';
                    }
                    $self->registro[] = 'db(\'' . $tabla . '\').campo(\'' . $nombre . '\',db.' . $rtype($tipo) . ',' . pyjslib_str($unico) . ',' . pyjslib_str($vacio) . ',' . pyjslib_str($unicaFila) . ',' . pyjslib_str($unicacolumna) . ',' . pyjslib_str($mini) . ',' . pyjslib_str($maxi) . ',' . pyjslib_str($step) . ',' . pyjslib_str($formato) . ')';
                    $self->rcampos[] = 'db(\'' . $tabla . '\').campo(\'' . $nombre . '\',db.' . $rtype($tipo) . ',' . pyjslib_str($unico) . ',' . pyjslib_str($vacio) . ',' . pyjslib_str($unicaFila) . ',' . pyjslib_str($unicacolumna) . ',' . pyjslib_str($mini) . ',' . pyjslib_str($maxi) . ',' . pyjslib_str($step) . ',' . pyjslib_str($formato) . ')';
                }
            }
            catch(Exception $e) {
                                pyjslib_printnl('');
                pyjslib_printnl('error al crear campos');
                pyjslib_printnl($e);
                $self->registro[] = 'db.campo(\'' . $nombre . '\',\'db.' . $rtype($tipo) . ',' . pyjslib_str($unico) . ',' . pyjslib_str($vacio) . ',' . pyjslib_str($unicaFila) . ',' . pyjslib_str($unicacolumna) . ',' . pyjslib_str($mini) . ',' . pyjslib_str($maxi) . ',' . pyjslib_str($step) . ',' . pyjslib_str($formato) . ')';
                $self->rcampos[] = 'db.campo(\'' . $nombre . '\',\'db.' . $rtype($tipo) . ',' . pyjslib_str($unico) . ',' . pyjslib_str($vacio) . ',' . pyjslib_str($unicaFila) . ',' . pyjslib_str($unicacolumna) . ',' . pyjslib_str($mini) . ',' . pyjslib_str($maxi) . ',' . pyjslib_str($step) . ',' . pyjslib_str($formato) . ')';
            }
            return $self;
        }
        
        function insertar($campos,...$args) {
            try {
                $campos =new copy($campos);
                $valido = true;
                if (!in_array('sob', $args)) {
                    $args['sob'] = false;
                }
                $lcampos = [];
                $razones = [];
                $temp = [];
                $c = 0;
                foreach( $campos as $elem ) {
                    if (($self->campos[$self->seleccion][$c][5] == true)) {
                        if (($campos->count($elem) > 1)) {
                            $valido = false;
                            break;
                        }
                    }
                    if (($self->campos[$self->seleccion][$c][4] == true)) {
                        if (($self->tablas[$self->seleccion] != [])) {
                            if ((tuple($self->obtenerFilasValores($campos[0], $self->seleccion)) == $campos)) {
                                $valido = false;
                                break;
                            }
                        }
                    }
                    $c += 1;
                }
                if (($valido == true)) {
                    $c = 0;
                    foreach( $campos as $elem ) {
                        try {
                            if (($self->campos[$self->seleccion][$c][3] == true)) {
                                try {
                                    if (($elem == null)) {
                                        $lcampos[] = new obj($elem, $self->dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                    }
                                    else {
                                        if (($self->campos[$self->seleccion][$c][2] == true)) {
                                            try {
                                                if (($args['sob'] == true)) {
                                                    try {
                                                        $bloqueados = [];
                                                        foreach( $self->obtenerColumna($self->obtenerCampos()[$c]) as $elem2 ) {
                                                            if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->object)) {
                                                                $bloqueados[] = $elem2->valor;
                                                            }
                                                        }
                                                        if (($bloqueados == [])) {
                                                            try {
                                                                if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) != $self->campos[$self->seleccion][$c][1]) && ('<type \'all\'>' != $self->campos[$self->seleccion][$c][1])) {
                                                                    if (($self->campos[$self->seleccion][$c][1] == $self->doc) && ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->str)) {
                                                                        $lcampos[] = new obj($elem, $self->doc);
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($self->campos[$self->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($self->dbtype($elem, $self->campos[$self->seleccion][$c][9])), 1, -1 - 1);
                                                                    }
                                                                }
                                                                else {
                                                                    if (($self->campos[$self->seleccion][$c][1] == $db->file)) {
                                                                        if (($self->load == false)) {
                                                                            $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                                            $b = $f->read();
                                                                            $f->close();
                                                                            $campos[$c] = 'file://' . $b;
                                                                            if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                                if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj('file://' . $b, $self->dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                                if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $self->campos[$self->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj('file://' . $b, $self->dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                                $lcampos[] = new obj('file://' . $b, $self->dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else {
                                                                            $lcampos[] = new obj($elem->replace('file://', ''), $self->dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                        }
                                                                    }
                                                                    else {
                                                                        if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                            if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                                                if (($elem >= $self->campos[$self->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj($elem, $self->dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else {
                                                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                        }
                                                                        else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                            if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                                                if (($elem >= $self->campos[$self->seleccion][$c][6]) && ($elem <= $self->campos[$self->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else {
                                                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                        }
                                                                        else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                            $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                        }
                                                                        else {
                                                                            $valido = false;
                                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                            catch(Exception $e) {
                                                                                                                                pyjslib_printnl('Error en el bloque vacio -> unico : nobloqueados ');
                                                                pyjslib_printnl($e);
                                                            }
                                                        }
                                                        else {
                                                            try {
                                                                if (in_array($elem, $bloqueados)) {
                                                                    $valido = false;
                                                                    $razones[] = pyjslib_str($elem) . ' se repite y es un campo unico';
                                                                }
                                                                else {
                                                                    if (($self->campos[$self->seleccion][$c][1] == $db->file)) {
                                                                        if (($self->load == false)) {
                                                                            $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                                            $b = $f->read();
                                                                            $f->close();
                                                                            $campos[$c] = 'file://' . $b;
                                                                            if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                                if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                                if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $self->campos[$self->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else {
                                                                            $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                        }
                                                                    }
                                                                    else {
                                                                        if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                            if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                                                if (($elem >= $self->campos[$self->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else {
                                                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                        }
                                                                        else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                            if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                                                if (($elem >= $self->campos[$self->seleccion][$c][6]) && ($elem <= $self->campos[$self->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else {
                                                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                        }
                                                                        else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                            $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                        }
                                                                        else {
                                                                            $valido = false;
                                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                            catch(Exception $e) {
                                                                                                                                pyjslib_printnl('Error en el bloque vacio -> unico sobrescribir : bloqueados ');
                                                                pyjslib_printnl($e);
                                                            }
                                                        }
                                                    }
                                                    catch(Exception $e) {
                                                                                                                pyjslib_printnl('Error en el bloque vacio -> unico sobrescribir : bloqueados ');
                                                        pyjslib_printnl($e);
                                                    }
                                                }
                                                else {
                                                    try {
                                                        if (in_array($elem, $self->obtenerColumna($self->campos[$self->seleccion][$c][0]))) {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' se repite y es un campo unico';
                                                        }
                                                        else {
                                                            if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) != $self->campos[$self->seleccion][$c][1]) && ('<type \'all\'>' != $self->campos[$self->seleccion][$c][1])) {
                                                                if (($self->campos[$self->seleccion][$c][1] == $self->doc) && ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->str)) {
                                                                    if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                        if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                                            $lcampos[] = new obj($elem, $self->doc);
                                                                        }
                                                                        else {
                                                                            $valido = false;
                                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                        }
                                                                    }
                                                                    else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                        if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                                            $lcampos[] = new obj($elem, $self->doc);
                                                                        }
                                                                        else {
                                                                            $valido = false;
                                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                        }
                                                                    }
                                                                    else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                        $lcampos[] = new obj($elem, $self->doc);
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else {
                                                                    $valido = false;
                                                                    $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($self->campos[$self->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($self->dbtype($elem, $self->campos[$self->seleccion][$c][9])), 1, -1 - 1);
                                                                }
                                                            }
                                                            else {
                                                                if (($self->campos[$self->seleccion][$c][1] == $db->file)) {
                                                                    if (($self->load == false)) {
                                                                        $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                                        $b = $f->read();
                                                                        $f->close();
                                                                        $campos[$c] = 'file://' . $b;
                                                                        if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                            if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6])) {
                                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                            if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $self->campos[$self->seleccion][$c][7])) {
                                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                            $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                        }
                                                                        else {
                                                                            $valido = false;
                                                                            $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                        }
                                                                    }
                                                                    else {
                                                                        $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                    }
                                                                }
                                                                else {
                                                                    if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                        if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                                            if (($elem >= $self->campos[$self->seleccion][$c][6])) {
                                                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else {
                                                                            if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                    }
                                                                    else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                        if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                                            if (($elem >= $self->campos[$self->seleccion][$c][6]) && ($elem <= $self->campos[$self->seleccion][$c][7])) {
                                                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else {
                                                                            if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                    }
                                                                    else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                    catch(Exception $e) {
                                                                                                                pyjslib_printnl('Error en el bloque vacio -> unico nosobrescribir : bloqueados ');
                                                        pyjslib_printnl($e);
                                                    }
                                                }
                                            }
                                            catch(Exception $e) {
                                                                                                pyjslib_printnl('Error en bloque vacio -> unico ');
                                                pyjslib_printnl($e);
                                            }
                                        }
                                        else {
                                            try {
                                                if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) != $self->campos[$self->seleccion][$c][1]) && ('<type \'all\'>' != $self->campos[$self->seleccion][$c][1])) {
                                                    if (($self->campos[$self->seleccion][$c][1] == $self->doc) && ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->str)) {
                                                        try {
                                                            if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                                    $lcampos[] = new obj($elem, $self->doc);
                                                                }
                                                                else {
                                                                    $valido = false;
                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                }
                                                            }
                                                            else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                                    $lcampos[] = new obj($elem, $self->doc);
                                                                }
                                                                else {
                                                                    $valido = false;
                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                }
                                                            }
                                                            else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                $lcampos[] = new obj($elem, $self->doc);
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                        catch(Exception $e) {
                                                                                                                        pyjslib_printnl('Error en bloque vacio -> no-unico -> tipo igual -> tipo doc <br>');
                                                        }
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($self->campos[$self->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($self->dbtype($elem, $self->campos[$self->seleccion][$c][9])), 1, -1 - 1);
                                                    }
                                                }
                                                else {
                                                    try {
                                                        if (($self->campos[$self->seleccion][$c][1] == $db->file)) {
                                                            if (($self->load == false)) {
                                                                $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                                $b = $f->read();
                                                                $f->close();
                                                                $campos[$c] = 'file://' . $b;
                                                                if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                    if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6])) {
                                                                        $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                    if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $self->campos[$self->seleccion][$c][7])) {
                                                                        $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                    $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                }
                                                                else {
                                                                    $valido = false;
                                                                    $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                }
                                                            }
                                                            else {
                                                                $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                            }
                                                        }
                                                        else {
                                                            if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                                    if (($elem >= $self->campos[$self->seleccion][$c][6])) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else {
                                                                    if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                            }
                                                            else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                                if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                                    if (($elem >= $self->campos[$self->seleccion][$c][6]) && ($elem <= $self->campos[$self->seleccion][$c][7])) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else {
                                                                    if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                            }
                                                            else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                    }
                                                    catch(Exception $e) {
                                                                                                                pyjslib_printnl('Error en bloque vacio -> no-unico -> tipo igual <br>');
                                                        pyjslib_printnl($e);
                                                    }
                                                }
                                            }
                                            catch(Exception $e) {
                                                                                                pyjslib_printnl('Error en bloque vacio -> no-unico <br>');
                                                pyjslib_printnl($e);
                                            }
                                        }
                                    }
                                }
                                catch(Exception $e) {
                                                                        pyjslib_printnl('Error en bloque vacio ');
                                    pyjslib_printnl($e);
                                }
                            }
                            else {
                                if (($self->campos[$self->seleccion][$c][2] == true)) {
                                    if (($args['sob'] == true)) {
                                        $bloqueados = [];
                                        foreach( $self->obtenerColumna($self->obtenerCampos()[$c]) as $elem2 ) {
                                            if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->object)) {
                                                $bloqueados[] = $elem2->valor;
                                            }
                                        }
                                        if (($bloqueados == [])) {
                                            if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) != $self->campos[$self->seleccion][$c][1]) && ('<type \'all\'>' != $self->campos[$self->seleccion][$c][1])) {
                                                if (($self->campos[$self->seleccion][$c][1] == $self->doc) && ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->str)) {
                                                    if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                        if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                            $lcampos[] = new obj($elem, $self->doc);
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                        if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                            $lcampos[] = new obj($elem, $self->doc);
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                        $lcampos[] = new obj($elem, $self->doc);
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($self->campos[$self->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($self->dbtype($elem, $self->campos[$self->seleccion][$c][9])), 1, -1 - 1);
                                                }
                                            }
                                            else {
                                                if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                    if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                    if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                        }
                                        else {
                                            if (in_array($elem, $bloqueados)) {
                                                $valido = false;
                                                $razones[] = pyjslib_str($elem) . ' se repite y es un campo unico';
                                            }
                                            else {
                                                if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                    if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                    if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                        }
                                    }
                                    else {
                                        if (in_array($elem, $self->obtenerColumna($self->campos[$self->seleccion][$c][0]))) {
                                            $valido = false;
                                            $razones[] = pyjslib_str($elem) . ' se repite y es un campo unico';
                                        }
                                        else {
                                            if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) != $self->campos[$self->seleccion][$c][1]) && ('<type \'all\'>' != $self->campos[$self->seleccion][$c][1])) {
                                                if (($self->campos[$self->seleccion][$c][1] == $self->doc) && ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->str)) {
                                                    if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                        if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                            $lcampos[] = new obj($elem, $self->doc);
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                        if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                            $lcampos[] = new obj($elem, $self->doc);
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                        $lcampos[] = new obj($elem, $self->doc);
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($self->campos[$self->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($self->dbtype($elem, $self->campos[$self->seleccion][$c][9])), 1, -1 - 1);
                                                }
                                            }
                                            else {
                                                if (($self->campos[$self->seleccion][$c][1] == $db->file)) {
                                                    if (($self->load == false)) {
                                                        $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                        $b = $f->read();
                                                        $f->close();
                                                        $campos[$c] = 'file://' . $b;
                                                        if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                            if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6])) {
                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                        else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                            if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $self->campos[$self->seleccion][$c][7])) {
                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                        else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                            $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else {
                                                        $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                    }
                                                }
                                                else {
                                                    if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                        if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                            if (($elem >= $self->campos[$self->seleccion][$c][6])) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                        else {
                                                            if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                    }
                                                    else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                        if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->int) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->float) || ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->long)) {
                                                            if (($elem >= $self->campos[$self->seleccion][$c][6]) && ($elem <= $self->campos[$self->seleccion][$c][7])) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                        else {
                                                            if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                    }
                                                    else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                                else {
                                    if (($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) != $self->campos[$self->seleccion][$c][1]) && ('<type \'all\'>' != $self->campos[$self->seleccion][$c][1])) {
                                        if (($self->campos[$self->seleccion][$c][1] == $self->doc) && ($self->dbtype($elem, $self->campos[$self->seleccion][$c][9]) == $self->str)) {
                                            if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                    $lcampos[] = new obj($elem, $self->doc);
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                    $lcampos[] = new obj($elem, $self->doc);
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                $lcampos[] = new obj($elem, $self->doc);
                                            }
                                            else {
                                                $valido = false;
                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                            }
                                        }
                                        else {
                                            $valido = false;
                                            $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($self->campos[$self->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($self->dbtype($elem, $self->campos[$self->seleccion][$c][9])), 1, -1 - 1);
                                        }
                                    }
                                    else {
                                        if (($self->campos[$self->seleccion][$c][1] == $db->file)) {
                                            if (($self->load == false)) {
                                                $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                $b = $f->read();
                                                $f->close();
                                                $campos[$c] = 'file://' . $b;
                                                if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                    if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6])) {
                                                        $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                    if (((count($elem) + count('file://')) >= $self->campos[$self->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $self->campos[$self->seleccion][$c][7])) {
                                                        $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                    $lcampos[] = new obj('file://' . $b, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = 'El campo: ' . pyjslib_str($self->campos[$self->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else {
                                                $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                            }
                                        }
                                        else {
                                            if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6])) {
                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else if (($self->campos[$self->seleccion][$c][6] != 0) && ($self->campos[$self->seleccion][$c][7] != -1)) {
                                                if ((count($elem) >= $self->campos[$self->seleccion][$c][6]) && (count($elem) <= $self->campos[$self->seleccion][$c][7])) {
                                                    $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else if (($self->campos[$self->seleccion][$c][6] == 0) && ($self->campos[$self->seleccion][$c][7] == -1)) {
                                                $lcampos[] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][9]));
                                            }
                                            else {
                                                $valido = false;
                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        catch(Exception $e) {
                                                        pyjslib_printnl('Error en bloque Principal');
                        }
                        $c += 1;
                    }
                }
                if (($valido == true)) {
                    $self->tablas[$self->seleccion][$self->clavePrimaria[$self->seleccion]] = $lcampos;
                    $self->clavePrimaria[$self->seleccion] += 1;
                    try {
                        if (($tabla != null)) {
                            $self->registro[] = 'db(\'' . $tabla . '\').insertar(' . array_slice(pyjslib_str($campos), 1, -1 - 1) . ')';
                            $self->consola('La inserciÃ³n de datos fue realizada con exito en la tabla 
 [1;31m ' . $self->seleccion . '
 Datos insertados:
' . pyjslib_str($campos) . ' [0m
', $self);
                        }
                    }
                    catch(Exception $e) {
                                                $self->registro[] = 'db.insertar(' . array_slice(pyjslib_str($campos), 1, -1 - 1) . ')';
                        $self->consola('La inserciÃ³n de datos fue realizada con exito en la tabla [1;31m' . $self->seleccion . '[0m 
 Datos insertados:
' . pyjslib_str($campos) . '
', $self);
                    }
                }
                else {
                    $self->consola('La inserciÃ³n de datos no puedo ser realizada en la tabla [1;31m' . $self->seleccion . '[0m .
Razones: 
 ' . pyjslib_str($razones) . '
', $self);
                }
                return $self;
            }
            catch(Exception $e) {
                                pyjslib_printnl('Error al insertar ');
                pyjslib_printnl($e);
            }
        }


            foreach( $self->registro as $elem ) {
                if (in_array('db(\'' . $tabla . '\').insertar(', $elem)) {
                    if (($self->debug == true)) {
                        pyjslib_printnl(['#se ha eliminado ', $self->registro[$c]], true);
        function modificarCampo($i,$columna,$campoNuevo,$tabla= $self::seleccion) {
            $campoNuevo = new copy($campoNuevo);
            if (($obtenerCampo($columna) != null)) {
                $self->tablas[$self->seleccion][$i][$obtenerCampo($columna)]->valor = $campoNuevo;
                $self->registro[] = 'db(\'' . $tabla . '\').modificarCampo(' . pyjslib_str($i) . ',\'' . $columna . '\',' . (type($campoNuevo) == $str) ? '\'' . $campoNuevo . '\'' : pyjslib_str($campoNuevo) . ')';
                $self->nmodif += 1;
            }
            else {
                pyjslib_printnl('esta columna ' . $columna . ' no existe en la tabla');
            }
        }
        function delFila($i,$tabla=$self->seleccion) {
            $c = 0;
            $ids = 0;
                    }
                    if (($ids == $i)) {
                        unset($self->registro[$c]);
                    }
                    $ids += 1;
                }
                else if (in_array('tabla=' . $tabla, array_slice($elem, $elem->find('\').relacionar('), null)) && in_array('id=' . pyjslib_str($i), array_slice($elem, $elem->find('\').relacionar('), null))) {
                    if (($self->debug == true)) {
                        pyjslib_printnl(['#se ha eliminado ', $self->registro[$c]], true);
                    }
                    unset($self->registro[$c]);
                }
                $c += 1;
            }
        }
        function modificarFila($id,...$campos) {
            $c = 0;
            foreach( $campos as $elem ) {
                foreach( $self->campos[$self->seleccion] as $elem2 ) {
                    pyjslib_printnl('<br>');
                    pyjslib_printnl($elem);
                    pyjslib_printnl('<br>');
                    if (($elem2[1] == $dbtype($elem, $self->campos[$self->seleccion][$c][8]))) {
                        if (($dbtype($elem[1], $self->campos[$self->seleccion][$c][8]) == $self->campos[$self->seleccion][$c][1])) {
                            $self->consola('modificarFila
 de: ' . pyjslib_str($self->tablas[$self->seleccion][$id][$c]) . ' a: ' . pyjslib_str(new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][8]))) . '
', $self);
                            $self->tablas[$self->seleccion][$id][$c] = new obj($elem, $dbtype($elem, $self->campos[$self->seleccion][$c][8]));
                        }
                    }
                    $c += 1;
                }
            }
            try {
                if (($tabla != null)) {
                    $self->registro[] = 'db(\'' . $tabla . '\').modificar(' . pyjslib_str($id) . ',' . array_slice(pyjslib_str($campos), 1, -1 - 1) . ')';
                }
            }
            catch(Exception $e) {
                                $self->registro[] = 'db.modificar(' . pyjslib_str($id) . ',' . array_slice(pyjslib_str($campos), 1, -1 - 1) . ')';
            }
            return $self;
        }
        function grabar($dbfile=$self->dbfile) {
            try {
                $clear();
                $self->registro->insert(3, 'db.load=True');
                $self->registro[] = 'db.load=False';
                $f = pyjslib_open($dbfile, 'w');
                $c = '';
                foreach( $self->registro as $elem ) {
                    $c .= $elem . '
';
                }
                $f->write($c);
                $f->close();
                $self->consola('La base de datos fue grabada con exito
', $self);
            }
            catch(Exception $e) {
                                pyjslib_printnl($e);
            }
        }
        function obtenerColumna($campo,$t=$self->seleccion) {
            $l = [];
            foreach( $self->mostrarTablas()[$t] as $i ) {
                $l[] = $self->mostrarTablas()[$t][$i][$self->obtenerCampo($campo, $t)];
            }
            if (($self->t != null)) {
                $self->consola('obtenerColumna ' . $self->t . '
' . pyjslib_str($l) . '
', $self);
            }
            return $l;
        }
        function obtenerCampo($campo,$t=$self->seleccion) {
            $c = 0;
            foreach( $self->campos[$t] as $elem ) {
                if (($campo == $elem[0])) {
                    if (($self->t != null)) {
                        $self->consola('obtenerCampo
' . pyjslib_str($c) . '
', $self);
                    }
                    return $c;
                }
                $c += 1;
            }
        }
        function obtenerFilasId($campo,$t=$self->seleccion) {
            $l = [];
            foreach( $self->mostrarTablas()[$t] as $elem ) {
                if (in_array($campo, $self->mostrarTablas()[$t][$elem])) {
                    $l[] = $elem;
                }
            }
            if (($self->t != null)) {
                $self->consola('obtenerFila
' . pyjslib_str($elem) . '
', $self);
            }
            return $l;
        }
        function obtenerFilas($campo,$t=$self->seleccion) {
            $l = $obtenerFilasId($campo, $t);
            $l2 = [];
            foreach( $l as $i ) {
                $l2[] = $self->tablas[$t][$i];
            }
            return $l2;
        }
        function obtenerFilasValores($campo,$t=$self->seleccion) {
            $l = $obtenerFilas($campo, $t);
            $l2 = [];
            foreach( $l as $fila ) {
                foreach( $fila as $o ) {
                    if ((type($o->valor) == $str)) {
                        if (in_array('mailto:', $o->valor) && (array_slice($o->valor, null, count('mailto:')) == 'mailto:')) {
                            $l2[] = array_slice($o->valor, count('mailto:'), null);
                        }
                        else if (in_array('password:', $o->valor) && (array_slice($o->valor, null, count('password:')) == 'password:')) {
                            $l2[] = array_slice($o->valor, count('password:'), null);
                        }
                        else if (in_array('datetime:', $o->valor) && (array_slice($o->valor, null, count('datetime:')) == 'datetime:')) {
                            $l2[] = array_slice($o->valor, count('datetime:'), null);
                        }
                        else if (in_array('date:', $o->valor) && (array_slice($o->valor, null, count('date:')) == 'date:')) {
                            $l2[] = array_slice($o->valor, count('date:'), null);
                        }
                        else if (in_array('time:', $o->valor) && (array_slice($o->valor, null, count('time:')) == 'time:')) {
                            $l2[] = array_slice($o->valor, count('time:'), null);
                        }
                        else {
                            $l2[] = $o->valor;
                        }
                    }
                    else {
                        $l2[] = $o->valor;
                    }
                }
            }
            return $l2;
        }
        function obtenerFilasValoresPuro($campo,$t=$self->seleccion) {
            $l = $obtenerFilas($campo, $t);
            $l2 = [];
            foreach( $l as $fila ) {
                foreach( $fila as $o ) {
                    $l2[] = $o->valor;
                }
            }
            return $l2;
        }
        function obtener($i,$campo,$t=$self->seleccion) {
            return $self->tablas[$t][$i][$obtenerCampo($campo, $t)]->valor;
        }
        function obtenerFilaValores($i,$t=$self->seleccion) {
            $l = [];
            foreach( $self->tablas[$t][$i] as $elem ) {
                if ((type($elem->valor) == $str)) {
                    if (in_array('mailto:', $elem->valor) && (array_slice($elem->valor, null, count('mailto:')) == 'mailto:')) {
                        $l[] = decode(array_slice($elem->valor, count('mailto:'), null));
                    }
                    else if (in_array('password:', $elem->valor) && (array_slice($elem->valor, null, count('password:')) == 'password:')) {
                        $l[] = decode(array_slice($elem->valor, count('password:'), null));
                    }
                    else if (in_array('datetime:', $elem->valor) && (array_slice($elem->valor, null, count('datetime:')) == 'datetime:')) {
                        $l[] = decode(array_slice($elem->valor, count('datetime:'), null));
                    }
                    else if (in_array('date:', $elem->valor) && (array_slice($elem->valor, null, count('date:')) == 'date:')) {
                        $l[] = array_slice($elem->valor, count('date:'), null);
                    }
                    else if (in_array('time:', $elem->valor) && (array_slice($elem->valor, null, count('time:')) == 'time:')) {
                        $l[] = decode(array_slice($elem->valor, count('time:'), null));
                    }
                    else {
                        $l[] = decode($elem->valor);
                    }
                }
                else if ((type($elem->valor) == $list)) {
                    foreach( enumerate($elem->valor) as list($k, $elem2) ) {
                        if ((type($elem2) == $str)) {
                            $elem->valor[$k] = decode($elem2);
                        }
                    }
                    $l[] = $elem->valor;
                }
                else if ((type($elem->valor) == $dict)) {
                    $temp = [];
                    foreach( $elem->valor as $elem2 ) {
                        if ((type($elem->valor[$elem2]) == $str)) {
                            $temp[decode($elem2)] = decode($elem->valor[$elem2]);
                        }
                        else {
                            $temp[decode($elem2)] = $elem->valor[$elem2];
                        }
                    }
                    $l[] = $temp;
                }
                else {
                    $l[] = $elem->valor;
                }
            }
            return $l;
        }
        function obtenerFilaValoresPuro($i,$t=$self->seleccion) {
            $l = [];
            foreach( $self->tablas[$t][$i] as $elem ) {
                $l[] = $elem->valor;
            }
            return $l;
        }
        function obtenerCampos($t=$self->seleccion) {
            $c = 0;
            $l = [];
            foreach( $self->campos[$t] as $elem ) {
                $l[] = $elem[0];
            }
            if (($self->t != null)) {
                $self->consola('obtenerCampos
' . pyjslib_str($l) . '
', $self);
            }
            return $l;
        }
        function mostrarTablas($mostrar=false,$padres=false,$seleccion=$self->seleccion) {
            $dtablas = [];
            foreach( $self->tablas as $elem ) {
                if (($padres == false)) {
                    $dtablas[$elem] = [];
                    foreach( $self->tablas[$elem] as $i ) {
                        $dtablas[$elem][$i] = [];
                        foreach( $self->tablas[$elem][$i] as $camp ) {
                            $dtablas[$elem][$i][] = $camp->valor;
                        }
                    }
                }
                else {
                    if (!in_array('.', $elem)) {
                        $dtablas[$elem] = [];
                        foreach( $self->tablas[$elem] as $i ) {
                            $dtablas[$elem][$i] = [];
                            foreach( $self->tablas[$elem][$i] as $camp ) {
                                $dtablas[$elem][$i][] = $camp->valor;
                            }
                        }
                    }
                }
            }
            if (($mostrar == false)) {
                return $dtablas;
            }
            else {
                return $dtablas[$seleccion];
            }
        }
        function clear() {
            if (($self->nmodif >= $self->limite)) {
                $l = [];
                $l2 = $self->rcampos;
                foreach( $self->tablas as $tabla ) {
                    foreach( $self->tablas[$tabla] as $i ) {
                        $l[] = 'db(\'' . $tabla . '\').insertar(' . array_slice(pyjslib_str($obtenerFilaValoresPuro($i, $tabla)), 1, -1 - 1) . ')';
                    }
                }
                $l2->extend($l);
                $l2->extend($self->lrelaciones);
                $self->registro = $l2;
                $self->nmodif = 0;
            }
        }
        function relacionar($i,$campo1,$args) {
            try {
                if (($self->obtenerCampo($args['campo'], $args['tabla']) != null)) {
                    if (in_array('id', $args)) {
                        if (in_array('campo', $args)) {
                            try {
                                if (($self->tablas[$args['tabla']][$args['id']][$self->obtenerCampo($args['campo'], $args['tabla'])]->tipo == $self->object)) {
                                    $self->consola('Ya existe una relaciÃ³n para este campo
', $self);
                                }
                                else {
                                    try {
                                        $self->tablas[$args['tabla']][$args['id']][$self->obtenerCampo($args['campo'], $args['tabla'])]->tipo = $self->object;
                                        $self->tablas[$self->seleccion][$i][$self->obtenerCampo($campo1)] = $self->tablas[$args['tabla']][$args['id']][$self->obtenerCampo($args['campo'], $args['tabla'])];
                                        $l = array_slice(pyjslib_str($args), 1, -1 - 1)->split(',');
                                        $c = '';
                                        foreach( $l as $elem ) {
                                            $c .= array_slice($elem->split(':')[0], 1, -1 - 1)->replace('"', '')->replace('\'', '') . '=' . $elem->split(':')[1] . ',';
                                        }
                                        if (($tabla != null)) {
                                            $self->registro[] = 'db(\'' . $tabla . '\').relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                            $self->consola('La relaciÃ³n fue efectuada con exito
', $self);
                                            $self->relaciones[$self->seleccion] = [$i, $campo1, $args['tabla'], $args['id'], $args['campo']];
                                            $self->relaciones[$args['tabla']] = [$args['id'], $args['campo'], $self->seleccion, $i, $campo1];
                                            $self->lrelaciones[] = 'db(\'' . $tabla . '\').relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                        }
                                    }
                                    catch(Exception $e) {
                                                                                pyjslib_printnl('Error relacionar en bloque tabla<br>');
                                        pyjslib_printnl($e);
                                        $self->registro[] = 'db.relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                        $self->consola('La relaciÃ³n fue efectuada con exito
', $self);
                                        $self->relaciones[$self->seleccion] = [$i, $campo1, $args['tabla'], $args['id'], $args['campo']];
                                        $self->relaciones[$args['tabla']] = [$args['id'], $args['campo'], $self->seleccion, $i, $campo1];
                                        $self->lrelaciones[] = 'db.relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                    }
                                }
                            }
                            catch(Exception $e) {
                                                                pyjslib_printnl('Error en relacionar en bloque campo<br>');
                                pyjslib_printnl($e->args);
                            }
                        }
                    }
                    else {
                        if (($self->tablas[$args['tabla']]->tipo == $self->object)) {
                            $self->consola('Ya existe una relacion para este campo
', $self);
                        }
                        else {
                            $self->tablas[$self->seleccion][$i][$self->obtenerCampo($campo1)] = $self->tablas[$args['tabla']];
                            $l = array_slice(pyjslib_str($args), 1, -1 - 1)->split(',');
                            $c = '';
                            foreach( $l as $elem ) {
                                $c .= array_slice($elem->split(':')[0], 1, -1 - 1)->replace('"', '')->replace('\'', '') . '=' . $elem->split(':')[1] . ',';
                            }
                            try {
                                if (($tabla != null)) {
                                    $self->registro[] = 'db(\'' . $tabla . '\').relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                    $self->consola('La relaciÃ³n fue efectuada con exito
');
                                    $self->relaciones[$self->seleccion] = [$i, $campo1, $args['tabla'], $args['id'], $args['campo']];
                                    $self->relaciones[$args['tabla']] = [$args['id'], $args['campo'], $self->seleccion, $i, $campo1];
                                }
                            }
                            catch(Exception $e) {
                                                                $self->registro[] = 'db.relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                $self->relaciones[$self->seleccion] = [$i, $campo1, $args['tabla'], $args['id'], $args['campo']];
                                $self->relaciones[$args['tabla']] = [$args['id'], $args['campo'], $self->seleccion, $i, $campo1];
                                $self->consola('La relaciÃ³n fue efectuada con exito
', $self);
                            }
                        }
                    }
                    return $self;
                }
                else {
                    pyjslib_printnl(['El campo ', $args['campo'], ' a relacionar no existe en la tabla ', $args['tabla']], true);
                }
            }
            catch(Exception $e) {
                                pyjslib_printnl('Error en relacionar ');
                pyjslib_printnl($e);
            }
        }
        $self->campo = $campo;
        $self->insertar = $insertar;
        $self->str = $str;
        $self->int = $int;
        $self->float = $float;
        $self->bool = $bool;
        $self->dict = $dict;
        $self->list = $list;
        $self->tuple = $tuple;
        $self->object = $object;
        $self->long = $long;
        $self->all = '<type \'all\'>';
        $self->password = '<type \'password\'>';
        $self->email = '<type \'email\'>';
        $self->time = '<type \'time\'>';
        $self->date = '<type \'date\'>';
        $self->datetime = '<type \'datetime\'>';
        $self->url = '<type \'url\'>';
        $self->file = '<type \'file\'>';
        $self->bin = '<type \'binary\'>';
        $self->doc = '<type \'doc\'>';
        $self->dbtype = $dbtype;
        $self->modificarFila = $modificarFila;
        $self->modificarCampo = $modificarCampo;
        $self->mostrarTablas = $mostrarTablas;
        $self->grabar = $grabar;
        $self->obtenerCampo = $obtenerCampo;
        $self->relacionar = $relacionar;
        $self->id = $id;
        $self->consola = $consola;
        $self->debug = $debug;
        $self->columna = $columna;
        $self->obtenerCampos = $obtenerCampos;
        $self->obtenerFilas = $obtenerFilas;
        $self->obtenerFilasId = $obtenerFilasId;
        $self->obtenerFilasValores = $obtenerFilasValores;
        $self->obtenerFilaValores = $obtenerFilaValores;
        $self->obtenerColumna = $obtenerColumna;
        $self->obtener = $obtener;
        $self->delFila = $delFila;
        $self->obtenerFormato = $obtenerFormato;
        $self->t = null;
        $self->limite = 1;
        return $self;
    }
    $db->tablas = [];
    $db->campos = [];
    $db->clavePrimaria = [];
    $db->seleccion = null;
    $db->dbfile = $dbfile;
    $db->log = [];
    $db->load = false;
    $db->modificacion = false;
    if (($dbfile == null)) {
        $db->registro = ['# -*- coding: utf-8 -*-', 'try:
 from ztec.zdb import DB
except:
 from zdb import DB', 'db=DB()'];
        $db->rcampos = ['# -*- coding: utf-8 -*-', 'try:
 from ztec.zdb import DB
except:
 from zdb import DB', 'db=DB()'];
    }
    else {
        $x = dbcargar($dbfile, $debug);
        if ((pyjslib_str(type($x)) != '<type \'function\'>')) {
            try {
                require_once( 'traceback.php');
                require_once( 'sys.php');
                list($exc_type, $exc_obj, $exc_tb) = $sys->exc_info();
                $fname = $exc_tb->tb_frame->f_code->co_filename;
                $db->log[] = 'Ocurrio un error al cargar la base de datos ' . $dbfile . '
' . pyjslib_str($x) . '
' . ''->join($traceback->format_exception($exc_type, $fname, $exc_tb));
                $db->errores[] = 'Ocurrio un error al cargar la base de datos ' . $dbfile . '
' . pyjslib_str($x) . '
' . ''->join($traceback->format_exception($exc_type, $fname, $exc_tb));
            }
            catch(Exception $e) {
                                $db->log[] = 'Ocurrio un error al cargar la base de datos ' . $dbfile . '
' . pyjslib_str($x);
                $db->errores[] = 'Ocurrio un error al cargar la base de datos ' . $dbfile . '
' . pyjslib_str($x) . '
' . ''->join($traceback->format_exception($exc_type, $fname, $exc_tb));
            }
        }
        else {
            $db = $x;
        }
    }
    return $db;
}
function dbcargar($dbfile=null,$debug=false,$log=[]) {
    if (($dbfile != null)) {
        $f = pyjslib_open($dbfile, 'r');
        $instrucciones = $f->read();
        $f->close();
        try {
            eval($instrucciones);
            $db->debug = $debug;
            $db->consola('--------------------------------------------
La base de datos fue cargada con exito
', $db);
            $db->t = null;
            $db->registro[] = 'db.load=True';
            return $db;
        }
        catch(Exception $e) {
                        if (($debug == true)) {
                pyjslib_printnl('ocurrio un error al cargar la base de datos');
                pyjslib_printnl($e);
            }
            else {
                return $e;
            }
        }
    }
}

