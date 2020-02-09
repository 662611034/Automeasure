package main
import (
    "fmt"
    "net"
)

func main(){
    conn, err := net.Dial("tcp", "192.168.0.11:5025")
    if err != nil{
        fmt.Printf("%s\n", err)
        return
    }

    sendMsg := "*IDN?\n"
    conn.Write([]byte(sendMsg))

    readBuf := make([]byte, 1024)
    readlen, err := conn.Read(readBuf)
    fmt.Println(string(readBuf[:readlen]))

    conn.Close()
}
