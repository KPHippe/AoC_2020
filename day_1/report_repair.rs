use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {

    let _example_input = "\
1721
979
366
299
675
1456 ";

    // let report: [i32;7] = [1721, 979, 366, 299, 675, 1456, 7];
    let report = parse_input("day_1_input.txt");

    let indices = find_two_2020(&report);
    let result = report[indices.0 as usize] * report[indices.1 as usize];
    println!("Two indices result: {}", result);

    let three_indices = find_three_2020(&report);
    let result = report[three_indices.0 as usize] * report[three_indices.1 as usize] * report[three_indices.2 as usize];
    println!("Three indices results: {}", result);

}

fn parse_input(input_path: &str) -> Vec<i32> {
    let path = Path::new(input_path);
    let display = path.display();

    let mut file = match File::open(&path) {
        Err(why) => panic!("Couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        // Not sure how to not print here, newbie to rust here!
        Ok(_) => print!(""),
    }

    let report: Vec<i32> = s.split_whitespace().map(|s| s.parse().expect("parse error")).collect();
    return report
}

fn find_two_2020(report: &[i32]) -> (i32, i32) {
    let target: i32 = 2020;

    for i in 0..report.len() {
        for j in 0..report.len(){
            if report[i] + report[j] == target {
                return (i as i32, j as i32);
            }
        }
    }
    (-1, -1)
}

fn find_three_2020(report: &[i32]) -> (i32, i32, i32) {
    let target: i32 = 2020;

    for x in 0..report.len() {
        for y in 0..report.len() {
            for z in 0..report.len() {
                if report[x] + report[y] + report[z] == target {
                    return (x as i32, y as i32, z as i32);
                }
            }
        }
    }
    (-1, -1, -1)
}
