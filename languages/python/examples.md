# EXAMPLES

inherit: (B da A)
class A:
    a=1
    class B(A):
    b=1




###
def main():
	…
if __name__=”__main__”:
	main()

ADVANTAGES:
identifiers defined in main are not global, so there’s no risk to use same names for variables from functions from either same file or imported files (which could be written by others or could be many and messy)
you can call main() from other files
you can import the file in another without running it (because if imported __name__!=”__main__”)


NOT WRITTEN RULES:
identifier named _ not to nìbe used (tmp)
a file is to be run only if it contains if__name__=”__main__”:
