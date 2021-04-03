use std::fs::OpenOptions;
use std::io::prelude::*;
use std::io::BufReader;
use std::vec::Vec;
use std::result::Result;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let f = OpenOptions::new().read(true).open("day1.txt")?;
	let reader = BufReader::new(f);
	let mut data: Vec<u16> = Vec::new();

	for line in reader.lines() {
		let i = u16::from_str_radix(&line?, 10);
		data.push(i?);
	}
	for i in &data {
		for j in &data {
			if i + j == 2020 {
				println!("{} + {} = 2020", i, j);
			}
		}
	}
	Ok(())
}