import QtQuick

Item {
    id: root
    property alias text: newText.text
    property alias font: newText.font
    property alias color: newText.color

    property color backgroundColor: theme.backgroundColor

    width: newText.width
    height: newText.height

    Rectangle {
        id: clipper
        width: root.width
        height: root.height
        clip: true
        color: root.backgroundColor

        Item {
            id: textContainer
            anchors.fill: parent

            Text {
                id: oldText
                anchors.centerIn: parent
                text: ""
                font: newText.font
                color: newText.color
                opacity: 0
            }

            Text {
                id: newText
                anchors.centerIn: parent
                text: ""
                font.pixelSize: 24
                color: "white"

                Behavior on text {
                    SequentialAnimation {
                        PropertyAnimation {
                            target: oldText
                            property: "y"
                            to: -root.height
                            duration: 300
                        }
                        ScriptAction {
                            script: oldText.text = newText.text
                        }
                        PropertyAnimation {
                            target: oldText
                            property: "y"
                            to: 0
                            duration: 0
                        }
                        PropertyAnimation {
                            target: newText
                            property: "y"
                            from: root.height
                            to: 0
                            duration: 300
                        }
                    }
                }
            }
        }
    }
}
