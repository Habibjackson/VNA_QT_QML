// import QtQuick
// import QtQuick.Controls.Material

// Button {
//     id: control
//     opacity: enabled ? 1.0 : 0.2

//     property int tripleWidth: width * 3

//     background: Rectangle {
//         radius: 24
//         color: theme.primaryColor
//         clip: true
//     }

//     onClicked: {
//         anim.start()
//     }

//     SequentialAnimation {
//         id: anim

//         // Expand the button
//         PropertyAnimation {
//             target: control
//             property: "scale"
//             to: 0.9
//             duration: 200
//             easing.type: Easing.InOutQuad
//         }

//         // Shrink back to normal
//         PropertyAnimation {
//             target: control
//             property: "scale"
//             to: 1.0
//             duration: 200
//             easing.type: Easing.InOutQuad
//         }
//     }

//     contentItem: Item {
//         implicitWidth: txt.implicitWidth
//         implicitHeight: 20

//         Text {
//             id: txt
//             anchors.centerIn: parent
//             text: control.text
//         }
//     }
// }
import QtQuick
import QtQuick.Controls

Button {
    id: control
    opacity: enabled ? 1.0 : 0.2

    property string variant: "default" // "default", "outlined", "text"
    property color bgColor: theme.primaryColor
    property color textColor: "white"
    property color borderColor: bgColor

    background: Rectangle {
        radius: 24
        color: variant === "text" ? "transparent" : bgColor
        border.color: variant === "outlined" ? borderColor : "transparent"
        border.width: variant === "outlined" ? 2 : 0
        clip: true
    }

    onClicked: anim.start()

    SequentialAnimation {
        id: anim
        PropertyAnimation {
            target: control
            property: "scale"
            to: 0.9
            duration: 200
            easing.type: Easing.InOutQuad
        }
        PropertyAnimation {
            target: control
            property: "scale"
            to: 1.0
            duration: 200
            easing.type: Easing.InOutQuad
        }
    }

    // ✅ SIMPLEST WAY TO CENTER TEXT
    contentItem: Text {
        text: control.text
        color: textColor
        font.pixelSize: 16
        font.bold: true
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        anchors.fill: parent
    }
}
