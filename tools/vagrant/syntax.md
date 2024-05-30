# SYNTAX

define an object `NAME` and work on it, calling it `machine` :
*	```ruby
	config.vm.define "NAME" do |machine|
		machine.PROPERTY = VALUE
		...
	end
	```

iterate :
*	```ruby
	(1..3).each do |i|
		config.vm.define "machine#{i}" do |machine|
			machine.vm.box = "debian/bookworm64"
			machine.vm.hostname = "hostname#{i}"
		end
	end
	```
	