import QtQuick.Controls.Material
import QtQuick

SpinBox {
    id: spinBox
    height: 50
    width: 200
    editable: true
    validator: IntValidator {
        bottom: spinBox.from
        top: spinBox.to
    }

    contentItem: TextInput {
        text: spinBox.textFromValue(spinBox.value, spinBox.locale)

        font: spinBox.font
        color: theme.textColor
        selectionColor: theme.textColor
        selectedTextColor: "#ffffff"
        horizontalAlignment: Qt.AlignHCenter
        verticalAlignment: Qt.AlignVCenter

        validator: spinBox.validator
    }

    up.indicator: Rectangle {
        implicitWidth: 40
        implicitHeight: 40
        radius: 20

        color: spinBox.up.hovered ? "#313131" : "transparent"
        x: spinBox.mirrored ? 0 : ((parent.width - width) - 5)
        y: ((spinBox.height - height) / 2)

        // color: theme.primaryColor
        Text {
            text: "+"
            font.pixelSize: spinBox.font.pixelSize * 2
            color: theme.textColor
            anchors.fill: parent
            fontSizeMode: Text.Fit
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }

    down.indicator: Rectangle {
        implicitWidth: 40
        implicitHeight: 40
        radius: 20

        color: spinBox.down.hovered ? "#313131" : "transparent"
        x: spinBox.mirrored ? ((parent.width - width) - 5) : 0
        y: ((spinBox.height - height) / 2)

        Text {
            text: "-"
            font.pixelSize: spinBox.font.pixelSize * 2
            color: theme.textColor
            anchors.fill: parent
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
    background: Rectangle {
        radius: 25
        color: "#1f1f1f"
    }
}
