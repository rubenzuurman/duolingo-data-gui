import generate_plots as gp

def main():
	lang_dict = gp.load_data("Rubenanz")
	lang_dict = gp.add_time_column(lang_dict)
	gp.export_plots(lang_dict, "Rubenanz")
	#print(lang_dict["korean"].columns)

if __name__ == "__main__":
	main()