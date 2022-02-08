import generate_plots as gp

def main():
	lang_dict = gp.load_data("Rubenanz")
	lang_dict = gp.add_time_column(lang_dict)
	print(lang_dict)

if __name__ == "__main__":
	main()