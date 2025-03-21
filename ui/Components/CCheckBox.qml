// import QtQuick
// import QtQuick.Controls

// CheckBox {
//     id: customCheckBox
//     text: ""
//     width: 24
//     height: 24
//     spacing: 10

//     indicator: Rectangle {
//         id: box
//         width: 24
//         height: 24
//         radius: 6
//         color: customCheckBox.checked ? "#1DB954" : "#333" // Spotify Green when checked
//         border.color: customCheckBox.checked ? "#1DB954" : "#888"
//         border.width: 2

//         Behavior on color {
//             ColorAnimation {
//                 duration: 150
//             }
//         }

//         Text {
//             text: "✔"
//             font.pixelSize: 18
//             color: "white"
//             visible: customCheckBox.checked
//             anchors.centerIn: parent
//         }
//     }

//     contentItem: Text {
//         text: customCheckBox.text
//         color: transparent
//         font.pixelSize: 14
//         opacity: enabled ? 1.0 : 0.3
//         leftPadding: 30
//     }
// }

import QtQuick
import QtQuick.Controls.Basic

CheckDelegate {
    id: control
    text: qsTr("CheckDelegate")
    checked: true

    contentItem: Text {
        rightPadding: control.indicator.width + control.spacing
        text: control.text
        font: control.font
        opacity: enabled ? 1.0 : 0.3
        color: control.checked ? "#1DB954" : "#333" // Spotify Green when checked
        elide: Text.ElideRight
        verticalAlignment: Text.AlignVCenter
    }

    indicator: Rectangle {
        implicitWidth: 26
        implicitHeight: 26
        x: control.width - width - control.rightPadding
        y: control.topPadding + control.availableHeight / 2 - height / 2
        radius: 3
        color: "transparent"
        // border.color: control.checked ? "#1DB954" : "#888"

        Rectangle {
            width: 14
            height: 14
            x: 6
            y: 6
            radius: 2
            color: control.down ? "#17a81a" : "#21be2b"
            visible: control.checked
        }
    }

    background: Rectangle {
        implicitWidth: 100
        implicitHeight: 40
        visible: control.down || control.highlighted
        color: control.down ? "#bdbebf" : "#eeeeee"
    }
}
