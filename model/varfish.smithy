$version: "2.0"

namespace com.example

use aws.protocols#restJson1

/// Echoes input
@restJson1
service EchoService {
    version: "2006-03-01"
    operations: [
        EchoMessage
    ]
}

@http(uri: "/echo", method: "POST")
operation EchoMessage {
    input := {
        @httpHeader("x-echo-message")
        message: String
    }

    output := {
        message: String
    }
}
