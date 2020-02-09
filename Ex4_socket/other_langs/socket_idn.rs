// https://riptutorial.com/rust/example/4404/a-simple-tcp-client-and-server-application--echo

use std::net::{TcpStream};
use std::io::{Read, Write};
use std::str::from_utf8;

fn main() {
    match TcpStream::connect("192.168.0.11:5025") {
        Ok(mut stream) => {
            println!("Successfully connected to server in port 5025");

            let msg = b"*IDN?\n";

            stream.write(msg).unwrap();
            println!("Sent Hello, awaiting reply...");

            let mut data = [0 as u8; 64]; // using 6 byte buffer
            match stream.read(&mut data) {
                Ok(_) => {
                    let text = from_utf8(&data).unwrap();
                    println!("{}", text);
                },
                Err(e) => {
                    println!("Failed to receive data: {}", e);
                }
            }
        },
        Err(e) => {
            println!("Failed to connect: {}", e);
        }
    }
    println!("Terminated.");
}
