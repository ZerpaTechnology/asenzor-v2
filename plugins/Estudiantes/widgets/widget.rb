#!/usr/bin/env  ruby
puts "Content-type: text/html\n\n"
puts """<div style='color:red'>"""
for i in 1..5
puts """
<h2>"""
puts "valor de la iteracion #{i}"
puts """</h2>
"""
end
puts """
</span>>"""

