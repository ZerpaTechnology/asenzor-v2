<?php

set_include_path(get_include_path() . PATH_SEPARATOR . dirname(__FILE__) . DIRECTORY_SEPARATOR . 'libpy2php');
require_once('py2php-master/libpy2php/libpy2php.php');
class ZDB{
	public $seleccion="defecto";
	public $error=[];

	public function ___construct($debug=false){
		$this->$seleccion=$seleccion;
        $this->error = $error;
        $this->debug=$debug;
        if (!in_array($tabla, $his->tablas) && !in_array($tabla, $his->campos)) {
            $his->campos[$tabla] = [];
            $his->clavePrimaria[$tabla] = 0;
            if (($herencia != null)) {
                $his->campos[$tabla] = copy::copy($his->campos[$herencia]);
            }
            $his->tablas[$tabla] = [];
            if (($copia != null)) {
                $his->tablas[$tabla] = copy::copy($his->tablas[$copia]);
                $his->clavePrimaria[$tabla] = (count($his->tablas[$tabla]) - 1);
            }
            $his->log = [];
            $his->nmodif = 0;
            $his->lrelaciones = [];
            $his->relaciones = [];
        }
        $his->seleccion = $tabla;
        $his->idseleccion = null;
	}
	public function consola($mensaje,$error=false) {
            $this->log[] = $mensaje;
            if (($his->debug == true)) {
                pyjslib_printnl($mensaje);
            }
            if ($error) {
                $this->errores[] = $mensaje;
            }
        }
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
            foreach( $his->campos[$his->seleccion] as $elem ) {
                if (($elem[0] == $campo)) {
                    return $elem[9];
                }
            }
        }
        function id($i) {
            $his->idseleccion = $i;
            return $his;
        }
        function columna($camp) {
            pyjslib_printnl($his->idseleccion);
            if (($his->t != null)) {
                $his->consola(pyjslib_str($his->tablas[$his->seleccion][$his->idseleccion][$his->obtenerCampo($camp)]) . '
', $his);
                return $his->tablas[$his->seleccion][$his->idseleccion][$his->obtenerCampo($camp)];
            }
        }
        function campo($nombre,$tipo,$unico=false,$vacio=true,$unicaFila=false,$unicacolumna=false,$mini=0,$maxi=-1,$step=null,$formato=null) {
            try {
                $his->campos[$his->seleccion][] = [$nombre, $tipo, $unico, $vacio, $unicaFila, $unicacolumna, $mini, $maxi, $step, $formato];
                if (($tabla != null)) {
                    if ((type($formato) == $str)) {
                        $formato = '\'' . $formato . '\'';
                    }
                    $his->registro[] = 'db(\'' . $tabla . '\').campo(\'' . $nombre . '\',db.' . $rtype($tipo) . ',' . pyjslib_str($unico) . ',' . pyjslib_str($vacio) . ',' . pyjslib_str($unicaFila) . ',' . pyjslib_str($unicacolumna) . ',' . pyjslib_str($mini) . ',' . pyjslib_str($maxi) . ',' . pyjslib_str($step) . ',' . pyjslib_str($formato) . ')';
                    $his->rcampos[] = 'db(\'' . $tabla . '\').campo(\'' . $nombre . '\',db.' . $rtype($tipo) . ',' . pyjslib_str($unico) . ',' . pyjslib_str($vacio) . ',' . pyjslib_str($unicaFila) . ',' . pyjslib_str($unicacolumna) . ',' . pyjslib_str($mini) . ',' . pyjslib_str($maxi) . ',' . pyjslib_str($step) . ',' . pyjslib_str($formato) . ')';
                }
            }
            catch(Exception $e) {
                                pyjslib_printnl('');
                pyjslib_printnl('error al crear campos');
                pyjslib_printnl($e);
                $his->registro[] = 'db.campo(\'' . $nombre . '\',\'db.' . $rtype($tipo) . ',' . pyjslib_str($unico) . ',' . pyjslib_str($vacio) . ',' . pyjslib_str($unicaFila) . ',' . pyjslib_str($unicacolumna) . ',' . pyjslib_str($mini) . ',' . pyjslib_str($maxi) . ',' . pyjslib_str($step) . ',' . pyjslib_str($formato) . ')';
                $his->rcampos[] = 'db.campo(\'' . $nombre . '\',\'db.' . $rtype($tipo) . ',' . pyjslib_str($unico) . ',' . pyjslib_str($vacio) . ',' . pyjslib_str($unicaFila) . ',' . pyjslib_str($unicacolumna) . ',' . pyjslib_str($mini) . ',' . pyjslib_str($maxi) . ',' . pyjslib_str($step) . ',' . pyjslib_str($formato) . ')';
            }
            return $his;
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
                    if (($his->campos[$his->seleccion][$c][5] == true)) {
                        if (($campos->count($elem) > 1)) {
                            $valido = false;
                            break;
                        }
                    }
                    if (($his->campos[$his->seleccion][$c][4] == true)) {
                        if (($his->tablas[$his->seleccion] != [])) {
                            if ((tuple($his->obtenerFilasValores($campos[0], $his->seleccion)) == $campos)) {
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
                            if (($his->campos[$his->seleccion][$c][3] == true)) {
                                try {
                                    if (($elem == null)) {
                                        $lcampos[] = new obj($elem, $his->dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                    }
                                    else {
                                        if (($his->campos[$his->seleccion][$c][2] == true)) {
                                            try {
                                                if (($args['sob'] == true)) {
                                                    try {
                                                        $bloqueados = [];
                                                        foreach( $his->obtenerColumna($his->obtenerCampos()[$c]) as $elem2 ) {
                                                            if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->object)) {
                                                                $bloqueados[] = $elem2->valor;
                                                            }
                                                        }
                                                        if (($bloqueados == [])) {
                                                            try {
                                                                if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) != $his->campos[$his->seleccion][$c][1]) && ('<type \'all\'>' != $his->campos[$his->seleccion][$c][1])) {
                                                                    if (($his->campos[$his->seleccion][$c][1] == $his->doc) && ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->str)) {
                                                                        $lcampos[] = new obj($elem, $his->doc);
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($his->campos[$his->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($his->dbtype($elem, $his->campos[$his->seleccion][$c][9])), 1, -1 - 1);
                                                                    }
                                                                }
                                                                else {
                                                                    if (($his->campos[$his->seleccion][$c][1] == $db->file)) {
                                                                        if (($his->load == false)) {
                                                                            $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                                            $b = $f->read();
                                                                            $f->close();
                                                                            $campos[$c] = 'file://' . $b;
                                                                            if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                                if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj('file://' . $b, $his->dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                                if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $his->campos[$his->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj('file://' . $b, $his->dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                                $lcampos[] = new obj('file://' . $b, $his->dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else {
                                                                            $lcampos[] = new obj($elem->replace('file://', ''), $his->dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                        }
                                                                    }
                                                                    else {
                                                                        if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                            if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                                                if (($elem >= $his->campos[$his->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj($elem, $his->dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else {
                                                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                        }
                                                                        else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                            if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                                                if (($elem >= $his->campos[$his->seleccion][$c][6]) && ($elem <= $his->campos[$his->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else {
                                                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                        }
                                                                        else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                            $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
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
                                                                    if (($his->campos[$his->seleccion][$c][1] == $db->file)) {
                                                                        if (($his->load == false)) {
                                                                            $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                                            $b = $f->read();
                                                                            $f->close();
                                                                            $campos[$c] = 'file://' . $b;
                                                                            if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                                if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                                if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $his->campos[$his->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else {
                                                                            $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                        }
                                                                    }
                                                                    else {
                                                                        if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                            if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                                                if (($elem >= $his->campos[$his->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else {
                                                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                        }
                                                                        else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                            if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                                                if (($elem >= $his->campos[$his->seleccion][$c][6]) && ($elem <= $his->campos[$his->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                            else {
                                                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                                }
                                                                                else {
                                                                                    $valido = false;
                                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                                }
                                                                            }
                                                                        }
                                                                        else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                            $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
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
                                                        if (in_array($elem, $his->obtenerColumna($his->campos[$his->seleccion][$c][0]))) {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' se repite y es un campo unico';
                                                        }
                                                        else {
                                                            if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) != $his->campos[$his->seleccion][$c][1]) && ('<type \'all\'>' != $his->campos[$his->seleccion][$c][1])) {
                                                                if (($his->campos[$his->seleccion][$c][1] == $his->doc) && ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->str)) {
                                                                    if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                        if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                                            $lcampos[] = new obj($elem, $his->doc);
                                                                        }
                                                                        else {
                                                                            $valido = false;
                                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                        }
                                                                    }
                                                                    else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                        if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                                            $lcampos[] = new obj($elem, $his->doc);
                                                                        }
                                                                        else {
                                                                            $valido = false;
                                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                        }
                                                                    }
                                                                    else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                        $lcampos[] = new obj($elem, $his->doc);
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else {
                                                                    $valido = false;
                                                                    $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($his->campos[$his->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($his->dbtype($elem, $his->campos[$his->seleccion][$c][9])), 1, -1 - 1);
                                                                }
                                                            }
                                                            else {
                                                                if (($his->campos[$his->seleccion][$c][1] == $db->file)) {
                                                                    if (($his->load == false)) {
                                                                        $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                                        $b = $f->read();
                                                                        $f->close();
                                                                        $campos[$c] = 'file://' . $b;
                                                                        if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                            if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6])) {
                                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                            if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $his->campos[$his->seleccion][$c][7])) {
                                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                            $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                        }
                                                                        else {
                                                                            $valido = false;
                                                                            $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                        }
                                                                    }
                                                                    else {
                                                                        $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                    }
                                                                }
                                                                else {
                                                                    if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                        if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                                            if (($elem >= $his->campos[$his->seleccion][$c][6])) {
                                                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else {
                                                                            if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                    }
                                                                    else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                        if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                                            if (($elem >= $his->campos[$his->seleccion][$c][6]) && ($elem <= $his->campos[$his->seleccion][$c][7])) {
                                                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                        else {
                                                                            if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                            }
                                                                            else {
                                                                                $valido = false;
                                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                            }
                                                                        }
                                                                    }
                                                                    else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
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
                                                if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) != $his->campos[$his->seleccion][$c][1]) && ('<type \'all\'>' != $his->campos[$his->seleccion][$c][1])) {
                                                    if (($his->campos[$his->seleccion][$c][1] == $his->doc) && ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->str)) {
                                                        try {
                                                            if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                                    $lcampos[] = new obj($elem, $his->doc);
                                                                }
                                                                else {
                                                                    $valido = false;
                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                }
                                                            }
                                                            else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                                    $lcampos[] = new obj($elem, $his->doc);
                                                                }
                                                                else {
                                                                    $valido = false;
                                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                }
                                                            }
                                                            else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                $lcampos[] = new obj($elem, $his->doc);
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
                                                        $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($his->campos[$his->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($his->dbtype($elem, $his->campos[$his->seleccion][$c][9])), 1, -1 - 1);
                                                    }
                                                }
                                                else {
                                                    try {
                                                        if (($his->campos[$his->seleccion][$c][1] == $db->file)) {
                                                            if (($his->load == false)) {
                                                                $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                                $b = $f->read();
                                                                $f->close();
                                                                $campos[$c] = 'file://' . $b;
                                                                if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                    if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6])) {
                                                                        $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                    if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $his->campos[$his->seleccion][$c][7])) {
                                                                        $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                    $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                }
                                                                else {
                                                                    $valido = false;
                                                                    $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                }
                                                            }
                                                            else {
                                                                $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                            }
                                                        }
                                                        else {
                                                            if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                                    if (($elem >= $his->campos[$his->seleccion][$c][6])) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else {
                                                                    if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                            }
                                                            else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                                if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                                    if (($elem >= $his->campos[$his->seleccion][$c][6]) && ($elem <= $his->campos[$his->seleccion][$c][7])) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                                else {
                                                                    if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                                    }
                                                                    else {
                                                                        $valido = false;
                                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                                    }
                                                                }
                                                            }
                                                            else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
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
                                if (($his->campos[$his->seleccion][$c][2] == true)) {
                                    if (($args['sob'] == true)) {
                                        $bloqueados = [];
                                        foreach( $his->obtenerColumna($his->obtenerCampos()[$c]) as $elem2 ) {
                                            if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->object)) {
                                                $bloqueados[] = $elem2->valor;
                                            }
                                        }
                                        if (($bloqueados == [])) {
                                            if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) != $his->campos[$his->seleccion][$c][1]) && ('<type \'all\'>' != $his->campos[$his->seleccion][$c][1])) {
                                                if (($his->campos[$his->seleccion][$c][1] == $his->doc) && ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->str)) {
                                                    if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                        if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                            $lcampos[] = new obj($elem, $his->doc);
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                        if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                            $lcampos[] = new obj($elem, $his->doc);
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                        $lcampos[] = new obj($elem, $his->doc);
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($his->campos[$his->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($his->dbtype($elem, $his->campos[$his->seleccion][$c][9])), 1, -1 - 1);
                                                }
                                            }
                                            else {
                                                if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                    if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                    if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
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
                                                if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                    if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                    if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                        }
                                    }
                                    else {
                                        if (in_array($elem, $his->obtenerColumna($his->campos[$his->seleccion][$c][0]))) {
                                            $valido = false;
                                            $razones[] = pyjslib_str($elem) . ' se repite y es un campo unico';
                                        }
                                        else {
                                            if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) != $his->campos[$his->seleccion][$c][1]) && ('<type \'all\'>' != $his->campos[$his->seleccion][$c][1])) {
                                                if (($his->campos[$his->seleccion][$c][1] == $his->doc) && ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->str)) {
                                                    if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                        if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                            $lcampos[] = new obj($elem, $his->doc);
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                        if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                            $lcampos[] = new obj($elem, $his->doc);
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                        $lcampos[] = new obj($elem, $his->doc);
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($his->campos[$his->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($his->dbtype($elem, $his->campos[$his->seleccion][$c][9])), 1, -1 - 1);
                                                }
                                            }
                                            else {
                                                if (($his->campos[$his->seleccion][$c][1] == $db->file)) {
                                                    if (($his->load == false)) {
                                                        $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                        $b = $f->read();
                                                        $f->close();
                                                        $campos[$c] = 'file://' . $b;
                                                        if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                            if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6])) {
                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                        else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                            if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $his->campos[$his->seleccion][$c][7])) {
                                                                $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                        else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                            $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                        }
                                                        else {
                                                            $valido = false;
                                                            $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                        }
                                                    }
                                                    else {
                                                        $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                    }
                                                }
                                                else {
                                                    if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                        if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                            if (($elem >= $his->campos[$his->seleccion][$c][6])) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                        else {
                                                            if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                    }
                                                    else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                        if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->int) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->float) || ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->long)) {
                                                            if (($elem >= $his->campos[$his->seleccion][$c][6]) && ($elem <= $his->campos[$his->seleccion][$c][7])) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                        else {
                                                            if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                            }
                                                            else {
                                                                $valido = false;
                                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                            }
                                                        }
                                                    }
                                                    else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                        $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
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
                                    if (($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) != $his->campos[$his->seleccion][$c][1]) && ('<type \'all\'>' != $his->campos[$his->seleccion][$c][1])) {
                                        if (($his->campos[$his->seleccion][$c][1] == $his->doc) && ($his->dbtype($elem, $his->campos[$his->seleccion][$c][9]) == $his->str)) {
                                            if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                    $lcampos[] = new obj($elem, $his->doc);
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                    $lcampos[] = new obj($elem, $his->doc);
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                $lcampos[] = new obj($elem, $his->doc);
                                            }
                                            else {
                                                $valido = false;
                                                $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                            }
                                        }
                                        else {
                                            $valido = false;
                                            $razones[] = pyjslib_str($elem) . ' tiene que ser ' . array_slice(pyjslib_str($his->campos[$his->seleccion][$c][1]), 1, -1 - 1) . ' y es ' . array_slice(pyjslib_str($his->dbtype($elem, $his->campos[$his->seleccion][$c][9])), 1, -1 - 1);
                                        }
                                    }
                                    else {
                                        if (($his->campos[$his->seleccion][$c][1] == $db->file)) {
                                            if (($his->load == false)) {
                                                $f = pyjslib_open($elem->replace('file://', ''), 'rb');
                                                $b = $f->read();
                                                $f->close();
                                                $campos[$c] = 'file://' . $b;
                                                if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                    if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6])) {
                                                        $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                    if (((count($elem) + count('file://')) >= $his->campos[$his->seleccion][$c][6]) && ((count($elem) + count('file://')) <= $his->campos[$his->seleccion][$c][7])) {
                                                        $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                    }
                                                    else {
                                                        $valido = false;
                                                        $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                    }
                                                }
                                                else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                    $lcampos[] = new obj('file://' . $b, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = 'El campo: ' . pyjslib_str($his->campos[$his->seleccion][$c]) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else {
                                                $lcampos[] = new obj($elem->replace('file://', ''), $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                            }
                                        }
                                        else {
                                            if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6])) {
                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else if (($his->campos[$his->seleccion][$c][6] != 0) && ($his->campos[$his->seleccion][$c][7] != -1)) {
                                                if ((count($elem) >= $his->campos[$his->seleccion][$c][6]) && (count($elem) <= $his->campos[$his->seleccion][$c][7])) {
                                                    $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
                                                }
                                                else {
                                                    $valido = false;
                                                    $razones[] = pyjslib_str($elem) . ' no cumple con los valores minimos y maximos establecidos.';
                                                }
                                            }
                                            else if (($his->campos[$his->seleccion][$c][6] == 0) && ($his->campos[$his->seleccion][$c][7] == -1)) {
                                                $lcampos[] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][9]));
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
                    $his->tablas[$his->seleccion][$his->clavePrimaria[$his->seleccion]] = $lcampos;
                    $his->clavePrimaria[$his->seleccion] += 1;
                    try {
                        if (($tabla != null)) {
                            $his->registro[] = 'db(\'' . $tabla . '\').insertar(' . array_slice(pyjslib_str($campos), 1, -1 - 1) . ')';
                            $his->consola('La inserciÃ³n de datos fue realizada con exito en la tabla 
 [1;31m ' . $his->seleccion . '
 Datos insertados:
' . pyjslib_str($campos) . ' [0m
', $his);
                        }
                    }
                    catch(Exception $e) {
                                                $his->registro[] = 'db.insertar(' . array_slice(pyjslib_str($campos), 1, -1 - 1) . ')';
                        $his->consola('La inserciÃ³n de datos fue realizada con exito en la tabla [1;31m' . $his->seleccion . '[0m 
 Datos insertados:
' . pyjslib_str($campos) . '
', $his);
                    }
                }
                else {
                    $his->consola('La inserciÃ³n de datos no puedo ser realizada en la tabla [1;31m' . $his->seleccion . '[0m .
Razones: 
 ' . pyjslib_str($razones) . '
', $his);
                }
                return $his;
            }
            catch(Exception $e) {
                                pyjslib_printnl('Error al insertar ');
                pyjslib_printnl($e);
            }
        }
        function modificarCampo($i,$columna,$campoNuevo,$tabla=null) {
            $campoNuevo = new copy($campoNuevo);
            if($tabla==null){
            	$tabla=$this->seleccion;
            }
            if (($obtenerCampo($columna) != null)) {
                $his->tablas[$his->seleccion][$i][$obtenerCampo($columna)]->valor = $campoNuevo;
                $his->registro[] = 'db(\'' . $tabla . '\').modificarCampo(' . pyjslib_str($i) . ',\'' . $columna . '\',' . (type($campoNuevo) == $str) ? '\'' . $campoNuevo . '\'' : pyjslib_str($campoNuevo) . ')';
                $his->nmodif += 1;
            }
            else {
                pyjslib_printnl('esta columna ' . $columna . ' no existe en la tabla');
            }
        }
        function delFila($i,$tabla=null) {
            $c = 0;
            $ids = 0;
            if($tabla==null){
            	$tabla=$his->seleccion;
            }
            foreach ($his->registro as $elem) {
            	if (strpos("db('".$tabla."').insertar(",$elem)==true){
            		if ($this->debug==True){
            			pyjslib_printnl("#se ha eliminado ", $this->registro[$c]);
            		}
                    if (($ids == $i)) {
                        unset($his->registro[$c]);
                    }
                    $ids += 1;
                    }
                
                else if (in_array('tabla=' . $tabla, array_slice($elem, $elem->find('\').relacionar('), null)) && in_array('id=' . pyjslib_str($i), array_slice($elem, $elem->find('\').relacionar('), null))) {
                    if (($his->debug == true)) {
                        pyjslib_printnl(['#se ha eliminado ', $his->registro[$c]], true);
                    }
                    unset($his->registro[$c]);
                }
                $c += 1;
            
        	}
        }
        function modificarFila($id,...$campos) {
            $c = 0;
            foreach( $campos as $elem ) {
                foreach( $his->campos[$his->seleccion] as $elem2 ) {
                    pyjslib_printnl('<br>');
                    pyjslib_printnl($elem);
                    pyjslib_printnl('<br>');
                    if (($elem2[1] == $dbtype($elem, $his->campos[$his->seleccion][$c][8]))) {
                        if (($dbtype($elem[1], $his->campos[$his->seleccion][$c][8]) == $his->campos[$his->seleccion][$c][1])) {
                            $his->consola('modificarFila
 de: ' . pyjslib_str($his->tablas[$his->seleccion][$id][$c]) . ' a: ' . pyjslib_str(new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][8]))) . '
', $his);
                            $his->tablas[$his->seleccion][$id][$c] = new obj($elem, $dbtype($elem, $his->campos[$his->seleccion][$c][8]));
                        }
                    }
                    $c += 1;
                }
            }
            try {
                if (($tabla != null)) {
                    $his->registro[] = 'db(\'' . $tabla . '\').modificar(' . pyjslib_str($id) . ',' . array_slice(pyjslib_str($campos), 1, -1 - 1) . ')';
                }
            }
            catch(Exception $e) {
                                $his->registro[] = 'db.modificar(' . pyjslib_str($id) . ',' . array_slice(pyjslib_str($campos), 1, -1 - 1) . ')';
            }
            return $his;
        }
        function grabar($dbfile=null) {
        	if($dbfile==null){
        		$dbfile=$his->dbfile;
        	}
            try {
                $clear();
                $his->registro->insert(3, 'db.load=True');
                $his->registro[] = 'db.load=False';
                $f = pyjslib_open($dbfile, 'w');
                $c = '';
                foreach( $his->registro as $elem ) {
                    $c .= $elem . '
';
                }
                $f->write($c);
                $f->close();
                $his->consola('La base de datos fue grabada con exito
', $his);
            }
            catch(Exception $e) {
                                pyjslib_printnl($e);
            }
        }
        function obtenerColumna($campo,$t=null) {
            $l = [];
            if($t===null){
            	$t=$his->seleccion;
            }
            foreach( $his->mostrarTablas()[$t] as $i ) {
                $l[] = $his->mostrarTablas()[$t][$i][$his->obtenerCampo($campo, $t)];
            }
            if (($his->t != null)) {
                $his->consola('obtenerColumna ' . $his->t . '
' . pyjslib_str($l) . '
', $his);
            }
            return $l;
        }
        function obtenerCampo($campo,$t=null) {
            $c = 0;
            if($t===null){
            	$t=$his->seleccion;
            }
            foreach( $his->campos[$t] as $elem ) {
                if (($campo == $elem[0])) {
                    if (($his->t != null)) {
                        $his->consola('obtenerCampo
' . pyjslib_str($c) . '
', $his);
                    }
                    return $c;
                }
                $c += 1;
            }
        }
        function obtenerFilasId($campo,$t=null) {
            $l = [];
            if($t===null){
            	$t=$his->seleccion;
            }
            foreach( $his->mostrarTablas()[$t] as $elem ) {
                if (in_array($campo, $his->mostrarTablas()[$t][$elem])) {
                    $l[] = $elem;
                }
            }
            if (($his->t != null)) {
                $his->consola('obtenerFila
' . pyjslib_str($elem) . '
', $his);
            }
            return $l;
        }
        function obtenerFilas($campo,$t=null) {
        	if($t===null){
            	$t=$his->seleccion;
            }
            $l = $obtenerFilasId($campo, $t);
            $l2 = [];
            foreach( $l as $i ) {
                $l2[] = $his->tablas[$t][$i];
            }
            return $l2;
        }
        function obtenerFilasValores($campo,$t=null) {
            $l = $obtenerFilas($campo, $t);
            $l2 = [];
            if($t===null){
            	$t=$his->seleccion;
            }
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
        function obtenerFilasValoresPuro($campo,$t=null) {
            $l = $obtenerFilas($campo, $t);
            $l2 = [];
            if($t===null){
            	$t=$his->seleccion;
            }
            foreach( $l as $fila ) {
                foreach( $fila as $o ) {
                    $l2[] = $o->valor;
                }
            }
            return $l2;
        }
        function obtener($i,$campo,$t=null) {
        	if($t===null){
            	$t=$his->seleccion;
            }
            return $his->tablas[$t][$i][$obtenerCampo($campo, $t)]->valor;
        }
        function obtenerFilaValores($i,$t=null) {
            $l = [];
            if($t===null){
            	$t=$his->seleccion;
            }
            foreach( $his->tablas[$t][$i] as $elem ) {
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
        function obtenerFilaValoresPuro($i,$t=null) {
            $l = [];
            if($t===null){
            	$t=$his->seleccion;
            }
            foreach( $his->tablas[$t][$i] as $elem ) {
                $l[] = $elem->valor;
            }
            return $l;
        }
        function obtenerCampos($t=null) {
            $c = 0;
            $l = [];
            if($t===null){
            	$t=$his->seleccion;
            }
            foreach( $his->campos[$t] as $elem ) {
                $l[] = $elem[0];
            }
            if (($his->t != null)) {
                $his->consola('obtenerCampos
' . pyjslib_str($l) . '
', $his);
            }
            return $l;
        }
        function mostrarTablas($mostrar=false,$padres=false,$seleccion=null) {
            $dtablas = [];
            if($seleccion===null){
            	$seleccion=$his->seleccion;
            }
            foreach( $his->tablas as $elem ) {
                if (($padres == false)) {
                    $dtablas[$elem] = [];
                    foreach( $his->tablas[$elem] as $i ) {
                        $dtablas[$elem][$i] = [];
                        foreach( $his->tablas[$elem][$i] as $camp ) {
                            $dtablas[$elem][$i][] = $camp->valor;
                        }
                    }
                }
                else {
                    if (!in_array('.', $elem)) {
                        $dtablas[$elem] = [];
                        foreach( $his->tablas[$elem] as $i ) {
                            $dtablas[$elem][$i] = [];
                            foreach( $his->tablas[$elem][$i] as $camp ) {
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
            if (($his->nmodif >= $his->limite)) {
                $l = [];
                $l2 = $his->rcampos;
                foreach( $his->tablas as $tabla ) {
                    foreach( $his->tablas[$tabla] as $i ) {
                        $l[] = 'db(\'' . $tabla . '\').insertar(' . array_slice(pyjslib_str($obtenerFilaValoresPuro($i, $tabla)), 1, -1 - 1) . ')';
                    }
                }
                $l2->extend($l);
                $l2->extend($his->lrelaciones);
                $his->registro = $l2;
                $his->nmodif = 0;
            }
        }
        function relacionar($i,$campo1,$args) {
            try {
                if (($his->obtenerCampo($args['campo'], $args['tabla']) != null)) {
                    if (in_array('id', $args)) {
                        if (in_array('campo', $args)) {
                            try {
                                if (($his->tablas[$args['tabla']][$args['id']][$his->obtenerCampo($args['campo'], $args['tabla'])]->tipo == $his->object)) {
                                    $his->consola('Ya existe una relaciÃ³n para este campo
', $his);
                                }
                                else {
                                    try {
                                        $his->tablas[$args['tabla']][$args['id']][$his->obtenerCampo($args['campo'], $args['tabla'])]->tipo = $his->object;
                                        $his->tablas[$his->seleccion][$i][$his->obtenerCampo($campo1)] = $his->tablas[$args['tabla']][$args['id']][$his->obtenerCampo($args['campo'], $args['tabla'])];
                                        $l = array_slice(pyjslib_str($args), 1, -1 - 1)->split(',');
                                        $c = '';
                                        foreach( $l as $elem ) {
                                            $c .= array_slice($elem->split(':')[0], 1, -1 - 1)->replace('"', '')->replace('\'', '') . '=' . $elem->split(':')[1] . ',';
                                        }
                                        if (($tabla != null)) {
                                            $his->registro[] = 'db(\'' . $tabla . '\').relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                            $his->consola('La relaciÃ³n fue efectuada con exito
', $his);
                                            $his->relaciones[$his->seleccion] = [$i, $campo1, $args['tabla'], $args['id'], $args['campo']];
                                            $his->relaciones[$args['tabla']] = [$args['id'], $args['campo'], $his->seleccion, $i, $campo1];
                                            $his->lrelaciones[] = 'db(\'' . $tabla . '\').relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                        }
                                    }
                                    catch(Exception $e) {
                                                                                pyjslib_printnl('Error relacionar en bloque tabla<br>');
                                        pyjslib_printnl($e);
                                        $his->registro[] = 'db.relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                        $his->consola('La relaciÃ³n fue efectuada con exito
', $his);
                                        $his->relaciones[$his->seleccion] = [$i, $campo1, $args['tabla'], $args['id'], $args['campo']];
                                        $his->relaciones[$args['tabla']] = [$args['id'], $args['campo'], $his->seleccion, $i, $campo1];
                                        $his->lrelaciones[] = 'db.relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
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
                        if (($his->tablas[$args['tabla']]->tipo == $his->object)) {
                            $his->consola('Ya existe una relacion para este campo
', $his);
                        }
                        else {
                            $his->tablas[$his->seleccion][$i][$his->obtenerCampo($campo1)] = $his->tablas[$args['tabla']];
                            $l = array_slice(pyjslib_str($args), 1, -1 - 1)->split(',');
                            $c = '';
                            foreach( $l as $elem ) {
                                $c .= array_slice($elem->split(':')[0], 1, -1 - 1)->replace('"', '')->replace('\'', '') . '=' . $elem->split(':')[1] . ',';
                            }
                            try {
                                if (($tabla != null)) {
                                    $his->registro[] = 'db(\'' . $tabla . '\').relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                    $his->consola('La relaciÃ³n fue efectuada con exito
');
                                    $his->relaciones[$his->seleccion] = [$i, $campo1, $args['tabla'], $args['id'], $args['campo']];
                                    $his->relaciones[$args['tabla']] = [$args['id'], $args['campo'], $his->seleccion, $i, $campo1];
                                }
                            }
                            catch(Exception $e) {
                                                                $his->registro[] = 'db.relacionar(' . pyjslib_str($i) . ',\'' . $campo1 . '\',' . $c . ')';
                                $his->relaciones[$his->seleccion] = [$i, $campo1, $args['tabla'], $args['id'], $args['campo']];
                                $his->relaciones[$args['tabla']] = [$args['id'], $args['campo'], $his->seleccion, $i, $campo1];
                                $his->consola('La relaciÃ³n fue efectuada con exito
', $his);
                            }
                        }
                    }
                    return $his;
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
	

}
$DB=new ZDB();

function db($tabla){
	
	#$GLOBALS['DB']->seleccion=$tabla;
	return $GLOBALS['DB'];

}


$db="db";
$db("tablas")->seleccion;
/*
$db("tablas")->show();
*/


?>