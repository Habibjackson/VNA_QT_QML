// import QtQuick
// import QtQuick.Controls
// import QtQuick.Layouts
// import "../Delegate"

// ColumnLayout {
//     spacing: 10
//     anchors.fill: parent

//     ListView {
//         id: listView
//         Layout.fillWidth: true
//         Layout.fillHeight: true
//         clip: true
//         currentIndex: 0
//         model: ListModel {
//             ListElement {
//                 name: "Single Port"
//                 value: "Tests the signle port of the antenna"
//             }
//             ListElement {
//                 name: "Double Port"
//                 value: "Tests the double port of the antenna"
//             }
//             ListElement {
//                 name: "Multitrace"
//                 value: "Tests the multiple port of the antenna with traces to compare"
//             }
//             ListElement {
//                 name: "Interband"
//                 value: "Tests between two ports"
//             }
//         }
//         delegate: TestsDelegate {}
//     }
// }
import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../Delegate"

ColumnLayout {
    spacing: 10
    Layout.fillWidth: true
    Layout.fillHeight: true

    Label {
        text: qsTr("Available Tests's")
        font.pixelSize: 16
        color: theme.textColorSecondary
        font.bold: true
        width: parent.width
        Layout.alignment: Qt.AlignLeft
        Layout.leftMargin: 12
    }

    ListView {
        id: listView
        Layout.fillWidth: true
        Layout.fillHeight: true
        clip: true
        model: ListModel {
            ListElement {
                name: "Single Port"
                value: "Tests the signle port of the antenna"
            }
            ListElement {
                name: "Double Port"
                value: "Tests the double port of the antenna"
            }
            ListElement {
                name: "Multitrace"
                value: "Tests the multiple port of the antenna with traces to compare"
            }
            ListElement {
                name: "Interband"
                value: "Tests between two ports"
            }
        }
        delegate: TestsDelegate {}
    }
}
