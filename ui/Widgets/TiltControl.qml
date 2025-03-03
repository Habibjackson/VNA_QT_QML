import QtQuick
import QtQuick.Controls.Material
import "../Components"

Paper {
    implicitWidth: columnLayout.implicitWidth + 20
    implicitHeight: columnLayout.implicitHeight + 20

    color: "#212121"

    Column {
        id: columnLayout
        spacing: 1
        anchors.centerIn: parent // Center the entire column

        Text {
            text: qsTr("Tilt Control")
            color: theme.textColor
        }
        CComboBox {
            model: ["first", "second"]
            width: parent.width
        }
        CSpinBox {}
        CButton {
            width: parent.width
            text: "Set Tilt"
            onClicked: console.log("clicked")
        }
    }
} // import QtQuick// import QtQuick.Controls// Frame {//     id: root//     width: 250//     height: 130//     padding: 10//     // Background with shadow effect//     Rectangle {//         id: backgroundRect//         color: "#f8f9fa" // Light gray background//         radius: 10//         anchors.fill: parent//         // Shadow effect using layer
//         layer.enabled: true
//         layer.effect: OpacityMask {
//             maskSource: backgroundRect
//         }
//         layer.smooth: true
//         layer.textureSizeMultiplier: 2.0
//     }

//     property alias buttonText: actionButton.text
//     property alias comboBoxModel: selectionBox.model
//     property alias spinBoxValue: valueBox.value
//     signal buttonClicked

//     Column {
//         anchors.fill: parent
//         spacing: 10

//         Row {
//             spacing: 5
//             Label {
//                 text: "Select:"
//                 width: 60
//                 verticalAlignment: Label.AlignVCenter
//             }
//             ComboBox {
//                 id: selectionBox
//                 width: 150
//                 model: ["Option 1", "Option 2", "Option 3"]
//             }
//         }

//         Row {
//             spacing: 5
//             Label {
//                 text: "Value:"
//                 width: 60
//                 verticalAlignment: Label.AlignVCenter
//             }
//             SpinBox {
//                 id: valueBox
//                 width: 80
//                 from: 0
//                 to: 100
//             }
//         }

//         Button {
//             id: actionButton
//             text: "Apply"
//             width: parent.width
//             background: Rectangle {
//                 id: buttonBg
//                 color: "#007bff" // Blue button
//                 radius: 5
//                 Behavior on color {
//                     ColorAnimation {
//                         duration: 200
//                     }
//                 }
//             }
//             MouseArea {
//                 anchors.fill: parent
//                 hoverEnabled: true
//                 onEntered: buttonBg.color = "#0056b3" // Darker blue on hover
//                 onExited: buttonBg.color = "#007bff"
//                 onClicked: root.buttonClicked()
//             }
//         }
//     }
// }

