import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

TextField {
    id: inputField
    height: 40
    Material.elevation: 0
    color: "white"
    placeholderText: ""
    font.pixelSize: 16

    background: Rectangle {
        id: bg
        height: parent.height
        color: "#1f1f1f"
        border.color: inputField.activeFocus ? "#fff" : "#555"
        border.width: inputField.activeFocus ? 2 : 0
        radius: 5
        Behavior on border.color { ColorAnimation { duration: 200 } }
    }
}
