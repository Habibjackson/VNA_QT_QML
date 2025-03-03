import QtQuick
import QtQuick.Controls.Material

ComboBox {
    id: control
    model: ["First", "Second", "Third"]

    delegate: ItemDelegate {
        width: control.width
        contentItem: Text {
            text: modelData
            color: theme.backgroundColorGrey2
            font: control.font
            elide: Text.ElideRight
            verticalAlignment: Text.AlignVCenter
        }
        highlighted: control.highlightedIndex === index
    }

    indicator: Canvas {
        id: canvas
        x: control.width - width - control.rightPadding
        y: control.topPadding + (control.availableHeight - height) / 2
        width: 12
        height: 8
        contextType: "2d"

        Connections {
            target: control
            function onPressedChanged() {
                canvas.requestPaint()
            }
        }

        onPaint: {
            context.reset()
            context.moveTo(0, 0)
            context.lineTo(width, 0)
            context.lineTo(width / 2, height)
            context.closePath()
            context.fillStyle = theme.backgroundColorGrey2
            context.fill()
        }
    }

    contentItem: Text {
        leftPadding: 16
        rightPadding: control.indicator.width + control.spacing

        text: control.displayText
        font: control.font
        color: theme.backgroundColorGrey2
        verticalAlignment: Text.AlignVCenter
        elide: Text.ElideRight
    }

    background: Rectangle {
        implicitWidth: 120
        implicitHeight: 40
        color: theme.backgroundColorGrey1
        radius: 4
    }

    popup: Popup {
        y: control.height - 1
        width: control.width
        implicitHeight: contentItem.implicitHeight
        padding: 1

        contentItem: ListView {
            clip: true
            implicitHeight: contentHeight
            model: control.popup.visible ? control.delegateModel : null
            currentIndex: control.highlightedIndex
            ScrollIndicator.vertical: ScrollIndicator {}
        }

        background: Rectangle {
            border.color: theme.backgroundColorGrey1
            radius: 4
            color: theme.backgroundColorGrey1
        }
    }
}
